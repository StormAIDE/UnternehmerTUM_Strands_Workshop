"""
Destination information tools - Mock implementations for workshop
Provides city guides, local tips, and currency information
"""
from strands import tool

# Import demo data
from demo_data.travel_info import CURRENCY_INFO, LOCAL_CUSTOMS, USEFUL_PHRASES
from demo_data.destinations import CITY_GUIDES, TRAVEL_TIPS


@tool
def city_guide(city: str) -> str:
    """
    Get a comprehensive city guide with key information.

    Args:
        city: City name

    Returns:
        City guide with highlights and tips
    """
    # Use centralized city guides from demo data
    guide = CITY_GUIDES.get(city.lower(), CITY_GUIDES["default"])

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
        category: Category (food, culture, nightlife, shopping, safety, photography)

    Returns:
        Local recommendations
    """
    # Use centralized travel tips from demo data
    tips = TRAVEL_TIPS.get(category.lower(), TRAVEL_TIPS["food"])

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
    # Use centralized currency data from demo_data
    country_key = country.title()

    # Get currency data or use generic fallback
    if country_key in CURRENCY_INFO:
        data = CURRENCY_INFO[country_key]
        currency_str = data["currency"]
        symbol = data["symbol"]
        payment_tip = data["tip"]
    else:
        # Generic fallback for countries not in demo data
        currency_str = "Local Currency"
        symbol = ""
        payment_tip = "Check exchange rates and carry some cash for small purchases"

    return f"""Currency Info for {country_key}:

💰 Currency: {currency_str} ({symbol})

💳 Payment Tips:
{payment_tip}

💡 Recommendations:
- Notify your bank before traveling
- Use ATMs in banks for better rates
- Keep some small bills for tips and small purchases
- Consider a travel credit card with no foreign fees
"""


@tool
def local_customs(country: str) -> str:
    """
    Get local customs and etiquette information for a country.

    Args:
        country: Country name

    Returns:
        Local customs and cultural etiquette tips
    """
    country_key = country.title()

    customs = LOCAL_CUSTOMS.get(country_key, [
        "Research local customs before arrival",
        "Observe and follow what locals do",
        "Be respectful of religious and cultural sites",
        "Learn a few basic phrases in the local language",
        "Dress appropriately for the culture"
    ])

    result = f"Local Customs & Etiquette for {country_key}:\n\n"
    for i, custom in enumerate(customs, 1):
        result += f"{i}. {custom}\n"

    return result


@tool
def useful_phrases(language: str) -> str:
    """
    Get useful phrases in the local language.

    Args:
        language: Language name (e.g., "Japanese", "German", "French")

    Returns:
        Common phrases with translations
    """
    language_key = language.title()

    phrases = USEFUL_PHRASES.get(language_key, {
        "Hello": "Hello",
        "Thank you": "Thank you",
        "Please": "Please",
        "Excuse me": "Excuse me",
        "Help": "Help"
    })

    result = f"Useful Phrases in {language_key}:\n\n"
    for english, translation in phrases.items():
        result += f"• {english}: {translation}\n"

    return result
