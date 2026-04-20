"""
Flight Agent - Handles flight search and booking
"""
from strands import Agent
import sys
import os

# Add parent directory to path to import tools
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.flight_tools import search_flights, book_flight, check_flight_availability


def create_flight_agent(model):
    """Create and return the Flight Agent"""
    system_prompt = """You are a Flight Booking Specialist.

Your role:
- Help users search for flights between cities
- Provide flight options with prices and schedules
- Assist with flight bookings
- Check availability for date ranges

Always be helpful, provide clear options, and confirm booking details before proceeding.
Format prices in euros (€) and times clearly."""

    agent = Agent(
        name="flight_agent",
        model=model,
        system_prompt=system_prompt,
        tools=[search_flights, book_flight, check_flight_availability]
    )

    return agent
