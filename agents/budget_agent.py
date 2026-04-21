"""
Budget Calculator Agent - Example using Strands Community Tools

This agent demonstrates how to use pre-built tools from strands-agents-tools package.
Participants can learn from this example when building their own agents.
"""
from strands import Agent
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ⭐ COMMUNITY TOOLS: Import from strands-agents-tools package
# No need to create custom @tool functions - just import and use!
from strands_tools.calculator import calculator
from strands_tools.current_time import current_time


def create_budget_agent(model):
    """Create and return the Budget Calculator Agent"""
    system_prompt = """You are a Travel Budget Calculator.

Your role:
- Help travelers estimate trip costs
- Calculate expenses using the calculator tool for accuracy
- Provide current date context using current_time tool when relevant
- Give clear budget breakdowns with percentages
- Suggest budget optimization tips

Always show your calculations step-by-step and format amounts clearly."""

    agent = Agent(
        name="budget_agent",
        model=model,
        system_prompt=system_prompt,
        tools=[
            calculator,      # Community tool for math operations
            current_time,    # Community tool for date/time info
        ]
    )

    return agent
