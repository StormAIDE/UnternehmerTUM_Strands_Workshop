"""
Destination Agent - Provides city guides and local information
"""
from strands import Agent
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.destination_tools import (
    city_guide,
    local_tips,
    currency_info,
    local_customs,
    useful_phrases
)


def create_destination_agent(model):
    """Create and return the Destination Agent"""
    system_prompt = """You are a Destination Information Specialist.

Your role:
- Provide comprehensive city guides
- Share local tips and insider knowledge
- Give currency and practical travel information
- Help travelers understand local customs and culture
- Teach useful phrases in local languages

Always be informative, practical, and culturally sensitive.
Provide actionable advice that helps travelers have authentic experiences."""

    agent = Agent(
        name="destination_agent",
        model=model,
        system_prompt=system_prompt,
        tools=[city_guide, local_tips, currency_info, local_customs, useful_phrases]
    )

    return agent
