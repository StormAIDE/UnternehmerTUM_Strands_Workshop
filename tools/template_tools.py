"""
Template Tools - YOUR CUSTOM TOOLS START HERE!

This file works together with agents/template_agent.py:
- Create your tools here
- Import them in agents/template_agent.py
- The app automatically uses your agent!

SIMPLE PATTERN:
1. Use @tool decorator
2. Add clear docstring (the AI reads this!)
3. Return helpful text

See other files in this folder (flight_tools.py, hotel_tools.py) for examples!
"""
from strands import tool


@tool
def get_travel_info(city: str, topic: str) -> str:
    """
    Get travel information about a city.

    Args:
        city: The city name
        topic: What to learn about (weather, culture, safety, etc.)

    Returns:
        Helpful information about the city
    """
    # Simple example: just return formatted text
    return f"""
    {topic.title()} information for {city}:

    - This is a helpful tip about {city}
    - Here's another useful piece of information
    - Don't forget to check local customs

    Have a great trip!
    """
