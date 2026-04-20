"""
TEMPLATE AGENT - YOUR CUSTOM AGENT STARTS HERE! ✨

This is where YOU build your own travel specialist agent!

INSTRUCTIONS:
1. Change AGENT_NAME to your agent's name
2. Update SYSTEM_PROMPT to describe what your agent does
3. Add your own @tool functions (or modify the example ones)
4. That's it! The orchestrator will automatically discover your agent.

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
    # TODO: Replace this with your logic!
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
    # TODO: Add your implementation here!
    return f"Processing query: {query}"


# ========================================
# Real Examples to Inspire You!
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
