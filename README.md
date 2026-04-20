# AWS Strands Agent Workshop - Travel Booking Assistant

Welcome to the **AWS Strands SDK Workshop**! In this hands-on session, you'll learn how to build AI agents using AWS Strands and create your own travel specialist agent.

---

## 🎁 **Ready-Made Resources for You!**

### Option 1: Use Our Demo Data
**Don't spend time creating mock data!** We've provided a complete `demo_data/` folder with:
- ✈️ Flights, 🏨 Hotels, 🍽️ Restaurants, 🎭 Attractions, ☀️ Weather, 🗺️ Travel Info

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
from strands_tools import calculator

agent = Agent(tools=[calculator])

```

---

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

### ⚡ IMPORTANT: Use Demo Data (No Mock Data Creation Needed!)

**We've provided ready-to-use datasets in the `demo_data/` folder so you can focus on learning Strands SDK!**

The `demo_data/` folder contains:
- ✈️ **Flights** - Airlines, routes, prices, schedules
- 🏨 **Hotels** - Hotels with ratings, amenities, prices
- 🍽️ **Restaurants** - Restaurant data with cuisines and reviews
- 🎭 **Attractions** - Tourist spots and activities
- ☀️ **Weather** - Seasonal weather patterns
- 🗺️ **Travel Info** - Visa requirements, phrases, packing lists, budgets

**📖 See `demo_data/README.md` for complete documentation and examples!**

**All existing agents (flight, hotel, weather) already use demo_data - check them out as examples!**

---

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

**Two easy options:**

**Option A: Use demo_data (recommended)**
```python
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

Add your tool to the agent:
```python
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
├── demo_data/                  # 🎯 Ready-to-use datasets!
│   ├── README.md              # How to use demo data
│   ├── restaurants.py         # Restaurant data
│   ├── attractions.py         # Tourist attractions
│   ├── travel_info.py         # Visa, phrases, packing
│   └── weather.py             # Weather patterns
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
| `travel_info.py` | Visa, phrases, packing lists, budgets | Travel prep agents |

### 🔍 How Existing Agents Use It:

**Flight Agent** uses:
```python
from demo_data.flights import AIRLINES, FLIGHT_ROUTES, DEPARTURE_TIMES
```

**Hotel Agent** uses:
```python
from demo_data.hotels import HOTELS, ROOM_TYPE_PRICES
```

**Weather Agent** uses:
```python
from demo_data.weather import SEASONAL_WEATHER
from demo_data.attractions import ATTRACTIONS, ACTIVITY_TYPES
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
from strands_community_tools import web_search

@tool
def search_restaurants(city: str, cuisine: str) -> str:
    """Search for restaurants using live web search."""
    query = f"best {cuisine} restaurants in {city}"
    return web_search(query)
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
- ✅ Use `eu-cantral-1` region (recommended)

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
