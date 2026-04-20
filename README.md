# AWS Strands Agent Workshop - Travel Booking Assistant

Welcome to the **AWS Strands SDK Workshop**! In this hands-on session, you'll learn how to build AI agents using AWS Strands and create your own travel specialist agent.

## 🎯 What You'll Build

A multi-agent travel booking system with:
- **Flight Agent** - Search and book flights
- **Hotel Agent** - Find and book accommodations
- **Itinerary Agent** - Plan activities and check weather
- **Destination Agent** - City guides and local tips
- **Your Custom Agent** - Build your own specialist!

## 📋 Prerequisites

- Python 3.9 or higher
- AWS Account with Bedrock access
- Basic Python knowledge (helpful but not required!)

---

## 🚀 Quick Start (5 Minutes)

### 1. Clone and Setup

```bash
# Navigate to workshop folder
cd UnternehmerTUM_Workshop

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure AWS Credentials

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` and add your AWS credentials:

```
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
BEDROCK_MODEL_ID=anthropic.claude-sonnet-4-20250514-v1:0
```

**Alternative:** If you have AWS CLI configured, the app will automatically use those credentials.

### 3. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### 4. Start Chatting!

1. Click **"Start Assistant"** button
2. Try example queries from the sidebar
3. Ask about flights, hotels, itineraries, or destinations!

---

## 🛠️ Workshop Challenge: Build Your Own Agent!

### Step 1: Choose Your Agent Idea

Pick one or create your own:
- 🍽️ **Restaurant Recommender** - Find best local restaurants
- 💰 **Budget Calculator** - Estimate trip costs
- ☀️ **Weather Advisor** - Weather-based travel tips
- 📋 **Visa Checker** - Check visa requirements
- 🗣️ **Language Phrasebook** - Essential local phrases
- 🚇 **Transport Guide** - Local transportation tips
- 📸 **Photo Spots Finder** - Instagram-worthy locations
- 🎒 **Packing List Generator** - Smart packing suggestions

### Step 2: Edit the Template

Open `agents/template_agent.py` and change **3 things**:

#### 1. Agent Name
```python
AGENT_NAME = "Restaurant Recommender"  # Change this
```

#### 2. System Prompt
```python
SYSTEM_PROMPT = """You are a Restaurant Recommendation Specialist.

Your role:
- Recommend restaurants based on cuisine preferences
- Consider budget constraints
- Provide information about local dining culture

Always provide 3-5 specific recommendations with details.
"""
```

#### 3. Create Tools
```python
@tool
def recommend_restaurants(city: str, cuisine: str, budget: str) -> str:
    """
    Recommend restaurants based on city, cuisine, and budget.
    
    Args:
        city: City name (e.g., "Paris", "Tokyo")
        cuisine: Type of cuisine (e.g., "italian", "japanese")
        budget: Budget level ("budget", "mid-range", "luxury")
    
    Returns:
        List of restaurant recommendations
    """
    # Your implementation here
    return f"Top {cuisine} restaurants in {city} for {budget} budget..."

# Add your tool to the agent
def create_template_agent(model):
    agent = Agent(
        name=AGENT_NAME,
        model=model,
        system_prompt=SYSTEM_PROMPT,
        tools=[
            recommend_restaurants,  # Your tool here!
        ]
    )
    return agent
```

### Step 3: Test Your Agent

1. Save the file (`Ctrl+S` or `Cmd+S`)
2. Restart Streamlit:
   ```bash
   # Press Ctrl+C to stop, then run again
   streamlit run app.py
   ```
3. Your agent is automatically registered! Try queries like:
   - "Recommend restaurants in Paris for Italian food"
   - "Find budget-friendly places in Tokyo"

---

## 📁 Project Structure

```
UnternehmerTUM_Workshop/
├── app.py                      # Streamlit web interface
├── orchestrator.py             # Main orchestrator agent
├── agents/
│   ├── flight_agent.py        # Flight search & booking
│   ├── hotel_agent.py         # Hotel search & booking
│   ├── itinerary_agent.py     # Trip planning
│   ├── destination_agent.py   # City guides
│   └── template_agent.py      # YOUR AGENT - start here!
├── tools/
│   ├── flight_tools.py        # Flight API tools
│   ├── hotel_tools.py         # Hotel API tools
│   └── weather_tools.py       # Weather API tools
├── .env.example                # Environment template
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────┐
│         STREAMLIT WEB UI                │
│           (app.py)                      │
└──────────────┬──────────────────────────┘
               │ User Query
               ▼
┌─────────────────────────────────────────┐
│      ORCHESTRATOR AGENT                 │
│      Routes requests to specialists     │
└──┬────┬────┬────┬───────────────────────┘
   │    │    │    │
   ▼    ▼    ▼    ▼
┌────┐┌────┐┌────┐┌────┐┌────────┐
│Flight│Hotel│Itinerary│Dest│ YOUR  │
│Agent││Agent││Agent ││Agent││ AGENT │
└──┬─┘└──┬─┘└──┬─┘└──┬─┘└───┬────┘
   │     │     │     │     │
   ▼     ▼     ▼     ▼     ▼
[Tools] [Tools] [Tools] [Tools] [Tools]
```

Each agent has specialized tools and can work independently or together!

---

## 💡 Tips for Building Great Agents

### 1. Write Clear System Prompts
Be specific about what your agent does:
```python
SYSTEM_PROMPT = """You are a [Role].
Your responsibilities:
- Task 1
- Task 2
Always provide [format] with [details]."""
```

### 2. Create Useful Tools
Tools are functions your agent can call:
```python
@tool
def my_tool(param: str) -> str:
    """
    Clear description of what this tool does.
    The AI reads this to decide when to use it!
    
    Args:
        param: Explain what this is
    
    Returns:
        Explain what you return
    """
    return "Your result"
```

### 3. Use Type Hints
Always include types (`param: str`, `-> str`). This helps the AI understand your tools.

### 4. Format Responses Well
- Use emojis for visual appeal (🎯, ✅, 💰)
- Use numbered lists for options
- Structure information clearly

### 5. Handle Errors Gracefully
```python
@tool
def my_tool(category: str) -> str:
    valid = ["option1", "option2"]
    if category not in valid:
        return f"Invalid. Choose from: {', '.join(valid)}"
    # Rest of code
```

---

## 💬 Example Queries to Try

### Flights
- "Find me flights from Munich to Tokyo in June"
- "What's available from Frankfurt to New York?"
- "Check flight availability for Barcelona in July"

### Hotels
- "Show me hotels in Paris for 3 nights"
- "Find a luxury hotel in Rome near the city center"
- "What are the best hotels in Barcelona?"

### Itineraries
- "Plan a 3-day itinerary for Amsterdam"
- "What activities can I do in Lisbon?"
- "What's the weather like in Berlin?"

### Destinations
- "Tell me about traveling to Tokyo"
- "What are must-see places in Barcelona?"
- "Local tips for Paris?"

---

## 🐛 Troubleshooting

### "Failed to initialize" error
- ✅ Check `.env` file exists with valid AWS credentials
- ✅ Verify Bedrock access in your AWS account
- ✅ Use `us-east-1` region (recommended)

### "Module not found" error
- ✅ Activate virtual environment: `source venv/bin/activate`
- ✅ Reinstall: `pip install -r requirements.txt`

### Agent not responding
- ✅ Click "Restart Agent" in sidebar
- ✅ Check AWS credentials haven't expired
- ✅ Look at terminal for error messages

### Custom agent not showing
- ✅ Save `template_agent.py` file
- ✅ Restart Streamlit app (Ctrl+C, then run again)
- ✅ Check for Python syntax errors

---

## 🎓 Learning Resources

- [Strands Documentation](https://strandsagents.com/docs/)
- [AWS Bedrock Guide](https://docs.aws.amazon.com/bedrock/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

## 📝 Next Steps After Workshop

1. ⭐ Star [Strands on GitHub](https://github.com/awslabs/strands)
2. 🔧 Add more tools to your agent
3. 🚀 Deploy your agent on AWS
4. 🌟 Share your creation!

---

## 🤝 Need Help?

- Check existing agents in `agents/` folder for examples
- Review tool implementations in `tools/` folder
- Ask your workshop instructor!

---

**Built with ❤️ using AWS Strands SDK | UnternehmerTUM Workshop 2026**
