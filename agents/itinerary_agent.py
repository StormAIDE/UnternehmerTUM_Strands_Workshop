"""
Itinerary Agent - Plans activities and provides weather info
"""
from strands import Agent
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.weather_tools import get_weather, suggest_activities, plan_itinerary


def create_itinerary_agent(model):
    """Create and return the Itinerary Agent"""
    system_prompt = """You are an Itinerary Planning Specialist.

Your role:
- Create day-by-day itineraries for trips
- Suggest activities based on user interests
- Provide weather forecasts to help planning
- Balance different types of activities (culture, food, nature, etc.)

Always consider the user's interests, time constraints, and travel style.
Provide practical timing suggestions and consider weather conditions."""

    agent = Agent(
        name="itinerary_agent",
        model=model,
        system_prompt=system_prompt,
        tools=[get_weather, suggest_activities, plan_itinerary]
    )

    return agent
