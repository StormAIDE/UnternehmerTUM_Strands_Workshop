"""
Travel Booking Assistant - Streamlit Web Interface
AWS Strands SDK Workshop
"""
import streamlit as st
import os
from dotenv import load_dotenv
from orchestrator import create_orchestrator, chat_with_orchestrator

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Travel Booking Assistant",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #FF6B35 0%, #F7931E 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .agent-card {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF6B35;
        color: white;
        border-radius: 5px;
        padding: 0.5rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #F7931E;
    }
</style>
""", unsafe_allow_html=True)


# Initialize session state
if 'orchestrator' not in st.session_state:
    st.session_state.orchestrator = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'initialized' not in st.session_state:
    st.session_state.initialized = False


def initialize_orchestrator():
    """Initialize the orchestrator agent"""
    try:
        with st.spinner("🚀 Initializing AI Travel Assistant..."):
            orchestrator = create_orchestrator()
            st.session_state.orchestrator = orchestrator
            st.session_state.initialized = True
            return True
    except Exception as e:
        st.error(f"❌ Failed to initialize: {str(e)}")
        st.info("Please check your .env file and AWS credentials.")
        return False


def main():
    # Header
    st.markdown('<h1 class="main-header">✈️ AI Travel Booking Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Powered by AWS Strands SDK & Amazon Bedrock</p>', unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.image("https://via.placeholder.com/300x100/FF6B35/FFFFFF?text=Travel+AI", use_container_width=True)

        st.markdown("## 🤖 Available Agents")

        agents_info = {
            "✈️ Flight Agent": "Search and book flights",
            "🏨 Hotel Agent": "Find and book hotels",
            "💰 Budget Agent": "Calculate trip costs (uses community tools!)",
            "🗺️ Destination Agent": "City guides and local tips",
            "⭐ Your Custom Agent": "Built by workshop participants!"
        }

        for agent, description in agents_info.items():
            st.markdown(f"**{agent}**")
            st.caption(description)
            st.markdown("---")

        st.markdown("## 💡 Example Queries")
        example_queries = [
            "Find flights from Munich to Tokyo in June",
            "Show me hotels in Paris for next week",
            "Calculate budget: flights 500€, hotel 300€/night 3 nights",
            "Tell me about local culture in Bangkok",
            "What are the best attractions in Rome?"
        ]

        for query in example_queries:
            if st.button(query, key=f"example_{query}"):
                st.session_state.selected_query = query

        st.markdown("---")
        st.markdown("### ⚙️ Configuration")

        if os.path.exists(".env"):
            st.success("✅ .env file found")
        else:
            st.warning("⚠️ .env file not found")

        model_id = os.getenv("BEDROCK_MODEL_ID", "Not configured")
        region = os.getenv("AWS_REGION", "Not configured")

        st.caption(f"**Model:** {model_id[:30]}...")
        st.caption(f"**Region:** {region}")

        if st.button("🔄 Restart Agent"):
            st.session_state.orchestrator = None
            st.session_state.initialized = False
            st.session_state.chat_history = []
            st.rerun()

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 💬 Chat with Travel Assistant")

        # Initialize orchestrator if not already done
        if not st.session_state.initialized:
            if st.button("🚀 Start Assistant", type="primary"):
                if initialize_orchestrator():
                    st.success("✅ Assistant ready! Start chatting below.")
                    st.rerun()
        else:
            # Chat interface
            chat_container = st.container()

            with chat_container:
                # Display chat history
                for i, (role, message) in enumerate(st.session_state.chat_history):
                    if role == "user":
                        st.chat_message("user").write(message)
                    else:
                        st.chat_message("assistant").write(message)

            # Chat input
            if 'selected_query' in st.session_state:
                user_message = st.session_state.selected_query
                del st.session_state.selected_query
            else:
                user_message = st.chat_input("Ask me anything about your travel plans...")

            if user_message:
                # Add user message to history
                st.session_state.chat_history.append(("user", user_message))

                # Display user message immediately
                st.chat_message("user").write(user_message)

                # Stream response from orchestrator
                from orchestrator import chat_with_orchestrator_stream_async
                import asyncio

                full_response = ""

                # Create async generator wrapper for Streamlit
                async def generate_response():
                    nonlocal full_response
                    async for text in chat_with_orchestrator_stream_async(
                        st.session_state.orchestrator,
                        user_message
                    ):
                        full_response = text
                        yield text

                # Convert async generator to sync for Streamlit
                def sync_generator():
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    try:
                        gen = generate_response()
                        while True:
                            try:
                                yield loop.run_until_complete(gen.__anext__())
                            except StopAsyncIteration:
                                break
                    finally:
                        loop.close()

                # Use Streamlit's write_stream for smooth streaming
                with st.chat_message("assistant"):
                    response = st.write_stream(sync_generator())

                # Add assistant response to history
                st.session_state.chat_history.append(("assistant", response))

                # Rerun to display the new messages properly
                st.rerun()

            # Clear chat button
            if st.session_state.chat_history:
                if st.button("🗑️ Clear Chat"):
                    st.session_state.chat_history = []
                    st.rerun()

    with col2:
        st.markdown("### 📊 Session Info")

        info_container = st.container()
        with info_container:
            st.metric("Total Messages", len(st.session_state.chat_history))

            if st.session_state.initialized:
                st.success("✅ Agent Active")
            else:
                st.warning("⏸️ Agent Not Started")

        st.markdown("---")
        st.markdown("### 🎓 Workshop Info")

        st.info("""
        **What to do:**
        1. Chat with the assistant
        2. See how agents work together
        3. Build your own custom agent
        4. Test it in this interface!

        **Edit:** `agents/template_agent.py`
        """)

        st.markdown("---")
        st.markdown("### 🔗 Resources")
        st.markdown("[📖 Strands Docs](https://strandsagents.com/docs/)")
        st.markdown("[🔧 AWS Bedrock](https://aws.amazon.com/bedrock/)")
        st.markdown("[🎨 Streamlit](https://streamlit.io/)")

    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; color: #666;">Built with ❤️ using AWS Strands SDK | '
        'UnternehmerTUM Workshop 2026</p>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
