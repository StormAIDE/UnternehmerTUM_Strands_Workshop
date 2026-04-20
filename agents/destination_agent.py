"""
Destination Agent - Provides city guides and local information
"""
from strands import Agent, tool


@tool
def city_guide(city: str) -> str:
    """
    Get a comprehensive city guide with key information.

    Args:
        city: City name

    Returns:
        City guide with highlights and tips
    """
    guides = {
        "paris": {
            "highlights": "Eiffel Tower, Louvre, Notre-Dame, Champs-Élysées",
            "best_time": "April-June, September-October",
            "local_tip": "Buy museum passes in advance to skip lines",
            "transport": "Metro is efficient and covers all major areas"
        },
        "tokyo": {
            "highlights": "Senso-ji Temple, Shibuya Crossing, Tokyo Tower, Tsukiji Market",
            "best_time": "March-May (cherry blossoms), October-November",
            "local_tip": "Get a Suica card for easy public transport",
            "transport": "Subway and JR lines are the best way to get around"
        },
        "barcelona": {
            "highlights": "Sagrada Familia, Park Güell, La Rambla, Gothic Quarter",
            "best_time": "May-June, September-October",
            "local_tip": "Book Gaudí attractions online to avoid long waits",
            "transport": "Metro and walking are perfect for exploring"
        },
        "default": {
            "highlights": "Historic center, local markets, museums, parks",
            "best_time": "Spring and fall typically offer great weather",
            "local_tip": "Ask locals for hidden gem recommendations",
            "transport": "Use public transport or walking tours"
        }
    }

    guide = guides.get(city.lower(), guides["default"])

    return f"""City Guide: {city.title()}

🎯 Must-See Highlights:
{guide['highlights']}

🌤️ Best Time to Visit:
{guide['best_time']}

💡 Local Tip:
{guide['local_tip']}

🚇 Getting Around:
{guide['transport']}
"""


@tool
def local_tips(city: str, category: str) -> str:
    """
    Get local tips for different categories.

    Args:
        city: City name
        category: Category (food, culture, nightlife, shopping)

    Returns:
        Local recommendations
    """
    tips_db = {
        "food": [
            "Try local street food markets for authentic cuisine",
            "Visit during lunch hours for better deals at restaurants",
            "Ask locals for their favorite neighborhood spots",
            "Don't skip the local breakfast specialties"
        ],
        "culture": [
            "Many museums offer free entry on certain days",
            "Join free walking tours to learn city history",
            "Check local event calendars for festivals",
            "Visit neighborhoods beyond the tourist center"
        ],
        "nightlife": [
            "Local bars often have happy hour deals",
            "Ask your hotel for safe nightlife areas",
            "Use official taxi or rideshare apps",
            "Clubs typically get busy after midnight"
        ],
        "shopping": [
            "Local markets offer better prices than tourist shops",
            "Negotiate at markets but be respectful",
            "Keep receipts for potential tax refunds",
            "Shop in local neighborhoods for unique finds"
        ]
    }

    tips = tips_db.get(category.lower(), tips_db["food"])

    result = f"Local Tips for {city.title()} - {category.title()}:\n\n"
    for i, tip in enumerate(tips, 1):
        result += f"{i}. {tip}\n"

    return result


@tool
def currency_info(country: str) -> str:
    """
    Get currency and payment information for a country.

    Args:
        country: Country name

    Returns:
        Currency and payment details
    """
    currencies = {
        "france": ("Euro (EUR)", "€", "Credit cards widely accepted, some small shops cash only"),
        "japan": ("Japanese Yen (JPY)", "¥", "Cash is king, carry yen for small shops and restaurants"),
        "spain": ("Euro (EUR)", "€", "Credit cards accepted, small amounts may need cash"),
        "usa": ("US Dollar (USD)", "$", "Credit cards everywhere, minimal cash needed"),
        "uk": ("British Pound (GBP)", "£", "Contactless payment very common, minimal cash needed"),
        "default": ("Local Currency", "", "Check exchange rates, carry some cash for small purchases")
    }

    currency_data = currencies.get(country.lower(), currencies["default"])

    return f"""Currency Info for {country.title()}:

💰 Currency: {currency_data[0]} ({currency_data[1]})

💳 Payment Tips:
{currency_data[2]}

💡 Recommendations:
- Notify your bank before traveling
- Use ATMs in banks for better rates
- Keep some small bills for tips and small purchases
- Consider a travel credit card with no foreign fees
"""


def create_destination_agent(model):
    """Create and return the Destination Agent"""
    system_prompt = """You are a Destination Information Specialist.

Your role:
- Provide comprehensive city guides
- Share local tips and insider knowledge
- Give currency and practical travel information
- Help travelers understand local customs and culture

Always be informative, practical, and culturally sensitive.
Provide actionable advice that helps travelers have authentic experiences."""

    agent = Agent(
        name="destination_agent",
        model=model,
        system_prompt=system_prompt,
        tools=[city_guide, local_tips, currency_info]
    )

    return agent
