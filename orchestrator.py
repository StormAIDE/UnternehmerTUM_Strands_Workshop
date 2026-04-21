"""
Orchestrator Agent - Routes requests to specialized agents
"""
from strands import Agent
from strands.models import BedrockModel
import os
from dotenv import load_dotenv

# Import specialized agents
from agents.flight_agent import create_flight_agent
from agents.hotel_agent import create_hotel_agent
from agents.budget_agent import create_budget_agent
from agents.destination_agent import create_destination_agent

# 🎯 WORKSHOP PARTICIPANTS: To add your custom agent:
# 1. Create your_agent.py in agents/ folder
# 2. Add import here: from agents.your_agent import create_your_agent
# 3. Create instance below (line ~57) and add to agents list

# Load environment variables
load_dotenv()


def create_orchestrator():
    """
    Create the main orchestrator agent with all specialized agents.

    The orchestrator routes user requests to the appropriate specialist agent.
    """
    # Configure Bedrock model
    model_id = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-sonnet-4-20250514-v1:0")
    aws_region = os.getenv("AWS_REGION", "us-east-1")

    print(f"🌍 Using AWS Region: {aws_region}")
    print(f"🤖 Using Model: {model_id}")

    # Note: AWS region is configured via AWS_REGION environment variable
    # Boto3 (used by BedrockModel) automatically reads AWS_REGION from environment

    # Add session token if provided (for temporary credentials)
    session_token = os.getenv("AWS_SESSION_TOKEN")
    if session_token:
        print("🔑 Using temporary AWS credentials with session token")

    try:
        model = BedrockModel(model_id=model_id)
    except Exception as e:
        print(f"Error initializing Bedrock model: {e}")
        print("Make sure your AWS credentials are configured correctly.")
        raise

    # Create all specialized agents
    flight_agent = create_flight_agent(model)
    hotel_agent = create_hotel_agent(model)
    budget_agent = create_budget_agent(model)  # Uses community tools!
    destination_agent = create_destination_agent(model)

    # 🎯 WORKSHOP PARTICIPANTS: Create your custom agent instances here
    # Example: restaurant_agent = create_restaurant_agent(model)

    # Add all agents to this list
    agents = [flight_agent, hotel_agent, budget_agent, destination_agent]
    # 🎯 WORKSHOP PARTICIPANTS: Add your agents here
    # Example: agents = [flight_agent, hotel_agent, itinerary_agent, destination_agent, restaurant_agent]

    # Create orchestrator with all agents as tools
    orchestrator_prompt = """You are a Travel Booking Orchestrator.

Your role is to help users plan and book their travel by coordinating with specialized agents.

When a user asks for help:
- Understand what they need
- Route the request to the appropriate specialist agent(s)
- You can use multiple agents if needed (e.g., flights + hotels + itinerary for a complete trip)
- Provide a helpful, friendly response

Always be conversational and helpful. If you're not sure which agent to use, ask clarifying questions.

You have access to various specialized agents - review their descriptions to understand what each can do.
"""

    orchestrator = Agent(
        name="travel_orchestrator",
        model=model,
        system_prompt=orchestrator_prompt,
        tools=agents  # Agents can be used as tools!
    )

    return orchestrator


def chat_with_orchestrator(orchestrator, message: str):
    """
    Send a message to the orchestrator and return the response.
    Non-streaming version for simple use cases.

    Args:
        orchestrator: The orchestrator agent
        message: User's message

    Returns:
        Agent's response text
    """
    try:
        result = orchestrator(message)
        # Extract text from message format
        if isinstance(result.message, dict) and 'content' in result.message:
            content = result.message['content']
            if isinstance(content, list) and len(content) > 0:
                return content[0].get('text', str(result.message))
        return str(result.message)
    except Exception as e:
        return f"Error processing request: {str(e)}"


async def chat_with_orchestrator_stream_async(orchestrator, message: str):
    """
    Send a message to the orchestrator and stream the response asynchronously.

    Yields the full accumulated text at each step for Streamlit to display.

    Args:
        orchestrator: The orchestrator agent
        message: User's message

    Yields:
        Full accumulated text at each streaming update
    """
    try:
        # Use stream_async to get real-time responses
        async for event in orchestrator.stream_async(message):
            # Extract and yield accumulated text from streaming events
            if isinstance(event, dict):
                # Check for data field (accumulated text generation)
                if "data" in event:
                    # Yield the full accumulated text
                    # Streamlit will handle displaying it progressively
                    yield event["data"]
    except Exception as e:
        yield f"\n\nError processing request: {str(e)}"


def chat_with_orchestrator_stream(orchestrator, message: str):
    """
    Synchronous wrapper for streaming (for non-async contexts).

    Args:
        orchestrator: The orchestrator agent
        message: User's message

    Yields:
        Text chunks as they are generated
    """
    import asyncio

    # Create or get event loop
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # Run the async generator
    async def run():
        async for chunk in chat_with_orchestrator_stream_async(orchestrator, message):
            yield chunk

    # Convert async generator to sync
    gen = run()
    while True:
        try:
            chunk = loop.run_until_complete(gen.__anext__())
            yield chunk
        except StopAsyncIteration:
            break


# Test function
if __name__ == "__main__":
    print("Initializing Travel Booking Orchestrator...")

    try:
        orchestrator = create_orchestrator()
        print("✅ Orchestrator initialized successfully!")
        print("\nTry asking: 'Find me flights from Munich to Tokyo'")
        print("\nStarting interactive chat (type 'exit' to quit):\n")

        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                break

            response = chat_with_orchestrator(orchestrator, user_input)
            print(f"\nAssistant: {response}\n")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nMake sure you have:")
        print("1. Created a .env file with AWS credentials")
        print("2. Installed all requirements (pip install -r requirements.txt)")
