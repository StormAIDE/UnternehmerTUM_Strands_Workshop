"""
TEMPLATE AGENT - YOUR CUSTOM AGENT STARTS HERE! ✨

This is where YOU build your own travel specialist agent!

INSTRUCTIONS:
1. Change AGENT_NAME to your agent's name
2. Update SYSTEM_PROMPT to describe what your agent does
3. Add your own @tool functions (or modify the example ones)
4. That's it! The orchestrator will automatically discover your agent.

💡 THREE EASY OPTIONS:
1. **Use demo_data** - Import from `demo_data/` folder (see `demo_data/README.md`)
2. **Simple strings** - Just return formatted text: `return f"Weather in {city}: Sunny, 25°C"`
3. **Community tools** - Use pre-built Strands tools (advanced): https://strandsagents.com/docs/user-guide/concepts/tools/community-tools-package/

Focus on learning Strands SDK, not creating data!

EXAMPLE IDEAS:
- Restaurant Recommender 🍽️
- Budget Calculator 💰
- Weather Advisor ☀️
- Visa Checker 📋
- Language Phrasebook 🗣️
- Transport Guide 🚇
- Photo Spots Finder 📸
- Packing List Generator 🎒
"""

from strands import Agent, tool

# Import demo data if you want to use it (optional!)
# from demo_data.restaurants import RESTAURANTS
# from demo_data.attractions import PHOTO_SPOTS
# from demo_data.travel_info import USEFUL_PHRASES
# See demo_data/README.md for all available data!


# ========================================
# CHANGE 1: Give your agent a name
# ========================================
AGENT_NAME = "template_agent"  # Change this! Use underscores, no spaces


# ========================================
# CHANGE 2: Write your system prompt
# ========================================
SYSTEM_PROMPT = """You are a helpful travel assistant.

Your role:
- Help travelers with [YOUR SPECIALTY HERE]
- Provide useful information and recommendations
- Be friendly and informative

[Add more details about what makes your agent unique!]
"""


# ========================================
# CHANGE 3: Define your tools
# ========================================
# Here are example tools - modify them or create your own!

@tool
def example_tool_one(city: str, param: str) -> str:
    """
    This is an example tool - replace with your own!

    Args:
        city: The city name
        param: Some parameter your tool needs

    Returns:
        Some useful information
    """
    # KEEP IT SIMPLE! Just return a string with basic info
    # The AI agent will use this to help the user
    return f"This is example output for {city} with parameter {param}"


@tool
def example_tool_two(query: str) -> str:
    """
    Another example tool - customize this!

    Args:
        query: User's query

    Returns:
        Response to the query
    """
    # DON'T overthink the mock data - simple strings work great!
    return f"Processing query: {query}"


# ========================================
# SIMPLE Examples - Easy to Copy! 🎯
# ========================================

# Example Using Demo Data
@tool
def get_photo_spots(city: str) -> str:
    """
    Find the best Instagram-worthy photo spots in a city.

    Args:
        city: City name

    Returns:
        List of photo spots
    """
    # Import the data right here if needed
    from demo_data.attractions import PHOTO_SPOTS

    # Get spots for the city, or provide generic suggestions
    spots = PHOTO_SPOTS.get(city, ["City Center", "Main Square", "Waterfront", "Historic District"])

    result = f"📸 Best Photo Spots in {city}:\n\n"
    for i, spot in enumerate(spots, 1):
        result += f"{i}. {spot}\n"

    result += "\n💡 Tip: Golden hour (sunrise/sunset) is best for photos!"
    return result


# Super Simple Example: Packing List
@tool
def suggest_packing_list(destination: str, days: int, season: str) -> str:
    """
    Suggest what to pack for a trip.

    Args:
        destination: Where the traveler is going
        days: Number of days
        season: summer, winter, spring, fall

    Returns:
        Packing suggestions
    """
    # See how simple this is? Just return helpful text!
    return f"""
    Packing List for {destination} ({days} days, {season}):

    Essentials:
    - Passport and travel documents
    - {days} sets of clothes
    - Comfortable walking shoes
    - Phone charger and adapter

    {season.title()} specific:
    - {'Sunscreen and hat' if season == 'summer' else 'Warm jacket and layers'}
    - {'Swimsuit' if season == 'summer' else 'Umbrella'}

    Don't forget: medications, toiletries, and a good book!
    """


# Another Simple Example: Local Phrases
@tool
def get_useful_phrases(destination: str) -> str:
    """
    Get useful local phrases for a destination.

    Args:
        destination: The country or city

    Returns:
        Common phrases in the local language
    """
    # You can use simple if/else or just return generic helpful info!
    return f"""
    Useful phrases for {destination}:

    - Hello / Goodbye
    - Please / Thank you
    - Where is...?
    - How much does this cost?
    - I don't speak [language]
    - Can you help me?
    - Do you speak English?

    Tip: Download a translation app before you go!
    """


# ========================================
# Slightly More Advanced Examples
# ========================================

# Example 1: Restaurant Recommender
@tool
def recommend_restaurants(city: str, cuisine: str, budget: str) -> str:
    """
    Recommend restaurants based on cuisine and budget.

    Args:
        city: City name
        cuisine: Type of cuisine (italian, japanese, local, etc.)
        budget: Budget level (budget, mid-range, luxury)

    Returns:
        Restaurant recommendations
    """
    # This is a mock implementation - in real app would call a restaurant API
    restaurants = {
        "budget": ["Local Tavern €€", "Street Food Market €", "Cozy Cafe €"],
        "mid-range": ["Bistro Central €€€", "Garden Restaurant €€€", "Rooftop Dining €€€"],
        "luxury": ["Michelin Star €€€€€", "Fine Dining Hall €€€€€"]
    }

    picks = restaurants.get(budget.lower(), restaurants["mid-range"])

    result = f"Top {cuisine.title()} Restaurants in {city} ({budget}):\n\n"
    for i, restaurant in enumerate(picks, 1):
        result += f"{i}. {restaurant}\n"

    return result


# Example 2: Budget Calculator
@tool
def calculate_trip_budget(destination: str, days: int, style: str) -> str:
    """
    Calculate estimated trip budget.

    Args:
        destination: Destination city/country
        days: Number of days
        style: Travel style (budget, moderate, luxury)

    Returns:
        Detailed budget breakdown
    """
    # Mock pricing based on style
    daily_costs = {
        "budget": {"accommodation": 50, "food": 30, "activities": 20, "transport": 15},
        "moderate": {"accommodation": 120, "food": 60, "activities": 50, "transport": 25},
        "luxury": {"accommodation": 300, "food": 150, "activities": 100, "transport": 50}
    }

    costs = daily_costs.get(style.lower(), daily_costs["moderate"])
    total_daily = sum(costs.values())
    total_trip = total_daily * days

    result = f"💰 Budget Estimate for {destination} ({days} days, {style} style):\n\n"
    result += "Per Day:\n"
    for category, amount in costs.items():
        result += f"  - {category.title()}: €{amount}\n"

    result += f"\nTotal per day: €{total_daily}\n"
    result += f"Total trip cost: €{total_trip}\n\n"
    result += "💡 Tip: Add 15-20% buffer for unexpected expenses!"

    return result


# ========================================
# Agent Creation Function
# ========================================
def create_template_agent(model):
    """
    Create and return your custom agent.

    The orchestrator calls this function to register your agent.
    """
    agent = Agent(
        name=AGENT_NAME,
        model=model,
        system_prompt=SYSTEM_PROMPT,
        tools=[
            # Add your tools here!
            example_tool_one,
            example_tool_two,
            # Uncomment these if you want to use the examples:
            # recommend_restaurants,
            # calculate_trip_budget,
        ]
    )

    return agent


# ========================================
# Quick Test (Optional)
# ========================================
if __name__ == "__main__":
    print(f"Testing {AGENT_NAME}...")
    print(f"System Prompt: {SYSTEM_PROMPT[:100]}...")
    print("\nYour agent is ready! Run the main app to see it in action.")
