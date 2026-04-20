"""
Hotel Agent - Handles hotel search and booking
"""
from strands import Agent
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.hotel_tools import find_hotels, check_rooms, book_hotel


def create_hotel_agent(model):
    """Create and return the Hotel Agent"""
    system_prompt = """You are a Hotel Booking Specialist.

Your role:
- Help users find hotels in their destination
- Provide hotel options with ratings and amenities
- Check room availability and types
- Assist with hotel bookings

Always provide detailed information about location, amenities, and cancellation policies.
Format prices clearly in euros (€)."""

    agent = Agent(
        name="hotel_agent",
        model=model,
        system_prompt=system_prompt,
        tools=[find_hotels, check_rooms, book_hotel]
    )

    return agent
