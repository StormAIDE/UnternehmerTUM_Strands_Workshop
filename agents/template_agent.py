"""
TEMPLATE AGENT - YOUR CUSTOM AGENT STARTS HERE!

Build your own travel specialist agent by editing 2 files:

1. tools/template_tools.py - Create your tools there
2. agents/template_agent.py - This file! Configure your agent below

The app automatically includes your agent. No need to touch any other files!

EXAMPLE IDEAS:
- Weather Advisor ☀️
- Restaurant Recommender 🍽️
- Budget Calculator 💰
- Packing List Generator 🎒
- Language Phrasebook 🗣️
"""

from strands import Agent
import sys
import os

# Add parent directory to path to import tools
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.template_tools import get_travel_info


# ========================================
# STEP 1: Give your agent a name
# ========================================
AGENT_NAME = "template_agent"  # Change this! Use underscores, no spaces


# ========================================
# STEP 2: Write your system prompt
# ========================================
SYSTEM_PROMPT = """You are a helpful travel assistant.

Your role:
- Help travelers with [YOUR SPECIALTY HERE]
- Provide useful information and recommendations
- Be friendly and informative

[Add more details about what makes your agent unique!]
"""


# ========================================
# STEP 3: Register your tools
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
            get_travel_info,  # Import your tools from tools/template_tools.py
        ]
    )

    return agent
