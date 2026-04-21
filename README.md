# AWS Strands Agent Workshop - Travel Booking Assistant

Welcome to the **AWS Strands SDK Workshop**! In this hands-on session, you'll learn how to build AI agents using AWS Strands and create your own travel specialist agent.

---

## 🎁 **Ready-Made Resources for You!**

### Option 1: Use Our Demo Data
**Don't spend time creating mock data!** We've provided a complete `demo_data/` folder with:
- ✈️ Flights, 🏨 Hotels, 🍽️ Restaurants, 🎭 Attractions, ☀️ Weather, 🗺️ Travel Info, 🌍 Destinations

**All existing agents already use this data** - just copy their pattern!

📖 **See [demo_data/README.md](demo_data/README.md) for complete guide with examples**

### Option 2: Use Strands Community Tools
**Use pre-built tools from Strands!** The community tools package has ready-to-use tools for:
- 🔍 Web search, Wikipedia, news
- 🖼️ Image generation and processing
- 📊 Data analysis and calculations
- 💬 Text processing
- And more!

📖 **Browse available tools: [Strands Community Tools](https://strandsagents.com/docs/user-guide/concepts/tools/community-tools-package/)**

```python
# Example: Using a community tool
from strands_tools.calculator import calculator

agent = Agent(tools=[calculator])
```

---

## 🎯 What You'll Build

A multi-agent travel booking system with:
- **Flight Agent** - Search and book flights
- **Hotel Agent** - Find and book accommodations
- **Budget Agent** - Calculate trip costs (uses community tools!)
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
AWS_REGION=eu-cantral-1
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

### 5. Explore Demo Data (Before Building Your Agent!)

```bash
# Open and read the demo data guide
cat demo_data/README.md

# Or open in your editor to see all available datasets
```

**All existing agents import from `demo_data/`** - look at `tools/flight_tools.py` line 8 to see how!

---

## 🛠️ Workshop Challenge: Build Your Own Agent!

### ✨ Simple Process - Create 2 New Files!

**You will create:**
1. `tools/your_agent_tools.py` - Create your tools
2. `agents/your_agent.py` - Configure your agent
3. Register in `orchestrator.py` - Add 3 lines of code

**That's it!** Follow the examples from existing agents. The template files are just reference - create your own!

---

## 🌟 Learn from Budget Agent (Community Tools Example!)

**The Budget Agent shows you how to use community tools!** Check out `agents/budget_agent.py`:

```python
# Import community tools - no custom @tool functions needed!
from strands_tools.calculator import calculator
from strands_tools.current_time import current_time

def create_budget_agent(model):
    agent = Agent(
        name="budget_agent",
        tools=[calculator, current_time]  # Just add them to the list!
    )
    return agent
```

**Key Learnings:**
1. ✅ No need to create `@tool` functions - just import
2. ✅ Community tools work seamlessly with custom agents
3. ✅ 46 tools available: calculator, http_request, file_read, etc.

**Try it:** "Calculate my trip budget: flights 500€, hotel 300€/night for 3 nights"

---

### ⚡ IMPORTANT: Use Demo Data (No Mock Data Creation Needed!)

**We've provided ready-to-use datasets in the `demo_data/` folder so you can focus on learning Strands SDK!**

The `demo_data/` folder contains:
- ✈️ **Flights** - Airlines, routes, prices, schedules
- 🏨 **Hotels** - Hotels with ratings, amenities, prices
- 🍽️ **Restaurants** - Restaurant data with cuisines and reviews
- 🎭 **Attractions** - Tourist spots and activities
- ☀️ **Weather** - Seasonal weather patterns
- 🗺️ **Travel Info** - Visa requirements, phrases, packing lists, budgets
- 🌍 **Destinations** - City guides, local tips by category

**📖 See `demo_data/README.md` for complete documentation and examples!**

**All existing agents (flight, hotel, weather) already use demo_data - check them out as examples!**

---

### Step 1: Choose Your Agent Idea

Pick one or create your own:
- 🍽️ **Restaurant Recommender** - Find best local restaurants
- 📅 **Itinerary Planner** - Plan day-by-day activities and schedules
- ☀️ **Weather Advisor** - Weather forecasts and packing suggestions
- 📋 **Visa Checker** - Check visa requirements by country
- 🗣️ **Language Phrasebook** - Essential local phrases and translations
- 🚇 **Transport Guide** - Local transportation tips and routes
- 📸 **Photo Spots Finder** - Instagram-worthy locations
- 🎒 **Packing List Generator** - Smart packing suggestions based on destination

### Step 2: Create Your Tool File

Create a new file `tools/restaurant_tools.py` (or your agent name):

**Option A: Use demo_data (recommended)**
```python
from strands import tool
from demo_data.restaurants import RESTAURANTS

@tool
def recommend_restaurants(city: str, budget: str) -> str:
    """Find restaurants in a city by budget level."""
    city_restaurants = RESTAURANTS.get(city, RESTAURANTS["default"])
    
    result = f"Top restaurants in {city} ({budget}):\n\n"
    for r in city_restaurants[:3]:  # Show top 3
        result += f"🍽️ {r['name']} - {r['cuisine']}\n"
        result += f"   {r['price']} • ⭐ {r['rating']}/5\n\n"
    return result
```

**Option B: Simple strings (no imports)**
```python
from strands import tool

@tool
def recommend_restaurants(city: str, cuisine: str, budget: str) -> str:
    """Recommend restaurants based on city, cuisine, and budget."""
    return f"""
    Top {cuisine} restaurants in {city} ({budget} budget):
    
    1. 🍽️ Local Bistro - Classic {cuisine} dishes
    2. 🍽️ Chef's Table - Modern {cuisine} cuisine
    3. 🍽️ Family Restaurant - Traditional favorites
    
    All highly rated and within your budget!
    """
```

**💡 See `demo_data/README.md` for more datasets and examples!**

### Step 3: Create Your Agent File

Create a new file `agents/restaurant_agent.py` (match your tool name):

```python
from strands import Agent
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.restaurant_tools import recommend_restaurants

AGENT_NAME = "restaurant_agent"

SYSTEM_PROMPT = """You are a Restaurant Recommendation Specialist.

Your role:
- Recommend restaurants based on cuisine preferences
- Consider budget constraints
- Provide information about local dining culture

Always provide 3-5 specific recommendations with details.
"""

def create_restaurant_agent(model):
    agent = Agent(
        name=AGENT_NAME,
        model=model,
        system_prompt=SYSTEM_PROMPT,
        tools=[
            recommend_restaurants,
        ]
    )
    return agent
```

### Step 4: Register in Orchestrator

Edit `orchestrator.py` to add your agent (3 simple edits):

**Edit 1: Add import (around line 14)**
```python
from agents.restaurant_agent import create_restaurant_agent
```

**Edit 2: Create instance (around line 64)**
```python
restaurant_agent = create_restaurant_agent(model)
```

**Edit 3: Add to agents list (same line 64)**
```python
agents = [flight_agent, hotel_agent, itinerary_agent, destination_agent, template_agent, restaurant_agent]
```

### Step 5: Test Your Agent

1. Save all three files (`Ctrl+S` or `Cmd+S`)
2. Restart Streamlit:
   ```bash
   # Press Ctrl+C to stop, then run again
   streamlit run app.py
   ```
3. Try queries like:
   - "Recommend restaurants in Paris for Italian food"
   - "Find budget-friendly places in Tokyo"

---

### 📝 Quick Reference: What Files to Look At

- **Community tools example**: `agents/budget_agent.py` ⭐ (uses calculator & current_time tools)
- **Custom tools examples**: `tools/flight_tools.py`, `tools/hotel_tools.py`
- **Example agents**: `agents/flight_agent.py`, `agents/hotel_agent.py`
- **Template files**: `tools/template_tools.py`, `agents/template_agent.py` (for reference only - create your own files!)
- **Demo data**: `demo_data/README.md` (all available datasets)

---


## 📁 Project Structure

```
UnternehmerTUM_Workshop/
├── app.py                      # Streamlit web interface
├── orchestrator.py             # Main orchestrator agent
├── agents/
│   ├── flight_agent.py        # Flight agent (imports flight_tools)
│   ├── hotel_agent.py         # Hotel agent (imports hotel_tools)
│   ├── budget_agent.py        # ⭐ Budget agent (uses community tools!)
│   ├── destination_agent.py   # City guides agent
│   └── template_agent.py      # 🎯 YOUR AGENT - Edit this!
├── tools/
│   ├── flight_tools.py        # Flight tools
│   ├── hotel_tools.py         # Hotel tools
│   └── template_tools.py      # 🎯 YOUR TOOLS - Create here!
├── demo_data/                  # 🎯 Ready-to-use datasets!
│   ├── README.md              # How to use demo data
│   ├── flights.py             # Airlines, routes, prices
│   ├── hotels.py              # Hotels with ratings, amenities
│   ├── restaurants.py         # Restaurant data
│   ├── attractions.py         # Tourist attractions
│   ├── weather.py             # Weather patterns
│   ├── travel_info.py         # Visa, phrases, packing, currency
│   └── destinations.py        # City guides, local tips
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
│Flight│Hotel│Budget│Dest│ YOUR  │
│Agent││Agent││Agent││Agent││ AGENT │
└──┬─┘└──┬─┘└──┬─┘└──┬─┘└───┬────┘
   │     │     │     │     │
   ▼     ▼     ▼     ▼     ▼
[Custom][Custom][Community][Custom][Your]
[Tools] [Tools]  [Tools]  [Tools] [Tools]
```

**Budget Agent uses community tools (calculator, current_time) - check it out!**

Each agent has specialized tools and can work independently or together!

---

## 🎯 Using Demo Data - The Easy Way!

**🎉 You don't need to create mock data from scratch!** The `demo_data/` folder contains ready-to-use datasets so you can focus on learning Strands SDK concepts.

### Why Demo Data?
- ✅ **No time wasted** creating mock data
- ✅ **Realistic data** with proper structure
- ✅ **Focus on learning** @tool, docstrings, Agent creation
- ✅ **All existing agents use it** - copy their patterns!

### Quick Example:
```python
from demo_data.attractions import PHOTO_SPOTS

@tool
def find_photo_spots(city: str) -> str:
    """Find Instagram-worthy photo spots."""
    spots = PHOTO_SPOTS.get(city, ["Main Square", "Waterfront", "Old Town"])
    return f"📸 Top spots in {city}:\n" + "\n".join(f"• {s}" for s in spots)
```

### 📦 Available Datasets:

| File | What's Inside | Use For |
|------|--------------|---------|
| `flights.py` | Airlines, routes, prices, schedules | Flight search agents |
| `hotels.py` | Hotels with ratings, amenities, room types | Hotel booking agents |
| `restaurants.py` | Restaurants with cuisines, ratings, prices | Food recommendation |
| `attractions.py` | Tourist spots, activities, photo locations | Itinerary planning |
| `weather.py` | Seasonal patterns, best visit times | Weather advisors |
| `travel_info.py` | Visa, phrases, packing lists, budgets, currency | Travel prep agents |
| `destinations.py` | City guides, local tips, best times to visit | Destination guides |

### 🔍 How Existing Agents Use It:

**Flight Agent** uses:
```python
from demo_data.flights import AIRLINES, FLIGHT_ROUTES, DEPARTURE_TIMES
```

**Hotel Agent** uses:
```python
from demo_data.hotels import HOTELS, ROOM_TYPE_PRICES
```

**Itinerary Agent** uses:
```python
from demo_data.weather import SEASONAL_WEATHER
from demo_data.attractions import ATTRACTIONS, ACTIVITY_TYPES
```

**Destination Agent** uses:
```python
from demo_data.travel_info import CURRENCY_INFO, LOCAL_CUSTOMS, USEFUL_PHRASES
from demo_data.destinations import CITY_GUIDES, TRAVEL_TIPS
```

### Three Options for Your Agent:

**Option 1: Use Demo Data (Recommended for Workshop)**
```python
from demo_data.restaurants import RESTAURANTS

@tool
def find_restaurants(city: str) -> str:
    """Find restaurants in a city."""
    city_restaurants = RESTAURANTS.get(city, RESTAURANTS["default"])
    result = f"Top restaurants in {city}:\n"
    for r in city_restaurants[:3]:
        result += f"🍽️ {r['name']} - {r['cuisine']} {r['price']}\n"
    return result
```

**Option 2: Simple Strings (Easiest)**
```python
@tool
def find_restaurants(city: str) -> str:
    """Find restaurants in a city."""
    return f"""
    Top restaurants in {city}:
    🍽️ Local Bistro - Great food!
    🍽️ Chef's Table - Fine dining
    🍽️ Street Food Market - Budget-friendly
    """
```

**Option 3: Strands Community Tools (Advanced)**
```python
from strands_tools.calculator import calculator

agent = Agent(tools=[calculator])
```

**📖 Resources:**
- Demo data: Read `demo_data/README.md` for all datasets and examples
- Community tools: Browse [Strands Community Tools](https://strandsagents.com/docs/user-guide/concepts/tools/community-tools-package/)

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

### Budget (Community Tools!)
- "Calculate my trip budget: flights 500€, hotel 300€/night for 3 nights, meals 60€/day"
- "What's today's date and estimate costs for next month trip?"
- "Budget breakdown for 5-day trip to Paris"

### Destinations
- "Tell me about traveling to Tokyo"
- "What are must-see places in Barcelona?"
- "Local tips for Paris?"

---

## 🐛 Troubleshooting

### "Failed to initialize" error
- ✅ Check `.env` file exists with valid AWS credentials
- ✅ Verify Bedrock access in your AWS account
- ✅ Use `eu-cantral-1` region (recommended)

### "Module not found" error
- ✅ Activate virtual environment: `source venv/bin/activate`
- ✅ Reinstall: `pip install -r requirements.txt`

### Agent not responding
- ✅ Click "Restart Agent" in sidebar
- ✅ Check AWS credentials haven't expired
- ✅ Look at terminal for error messages

### Custom agent not showing
- ✅ Save `<Your_Agent>.py` file
- ✅ Restart Streamlit app (Ctrl+C, then run again)
- ✅ Check for Python syntax errors

---

## 🎓 Learning Resources

### Strands SDK:
- [Strands Documentation](https://strandsagents.com/docs/)
- [Strands Community Tools Package](https://strandsagents.com/docs/user-guide/concepts/tools/community-tools-package/) - Pre-built tools you can use
- [Strands GitHub Repository](https://github.com/awslabs/strands)

### Other Technologies:
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
