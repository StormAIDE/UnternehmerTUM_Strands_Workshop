"""
Weather and itinerary tools - Mock implementations
"""
from strands import tool
import random
from datetime import datetime

# Import demo data
from demo_data.weather import SEASONAL_WEATHER, WEATHER_ACTIVITIES


@tool
def get_weather(city: str, date: str) -> str:
    """
    Get weather forecast for a city on a specific date.

    Args:
        city: City name
        date: Date in YYYY-MM-DD format

    Returns:
        Weather forecast details
    """
    # Determine season from date
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        month = date_obj.month
        if month in [3, 4, 5]:
            season = "spring"
        elif month in [6, 7, 8]:
            season = "summer"
        elif month in [9, 10, 11]:
            season = "fall"
        else:
            season = "winter"
    except:
        season = "summer"  # Default

    # Get seasonal weather from demo data
    city_weather = SEASONAL_WEATHER.get(city, {})
    season_data = city_weather.get(season, {
        "temp_range": "15-25°C",
        "conditions": "Pleasant weather",
        "clothing": "Light layers"
    })

    # Parse temperature range
    temp_range = season_data["temp_range"]
    conditions = season_data["conditions"]

    return (
        f"Weather Forecast for {city}\n"
        f"Date: {date} ({season.title()})\n\n"
        f"Temperature: {temp_range}\n"
        f"Conditions: {conditions}\n"
        f"Recommended Clothing: {season_data['clothing']}\n"
        f"Precipitation: {random.randint(0, 30)}%\n"
        f"Wind: {random.randint(5, 20)} km/h"
    )


@tool
def suggest_activities(city: str, interests: str) -> str:
    """
    Suggest activities and attractions in a city based on interests.

    Args:
        city: City name
        interests: Comma-separated interests (e.g., "culture, food, nature")

    Returns:
        Suggested activities
    """
    from demo_data.attractions import ACTIVITY_TYPES, ATTRACTIONS

    # Parse interests
    interest_list = [i.strip().lower() for i in interests.split(",")]
    suggestions = []

    # Get city-specific attractions first
    if city in ATTRACTIONS:
        city_attractions = ATTRACTIONS[city]
        suggestions.extend([a["name"] for a in city_attractions[:3]])

    # Add interest-based activities
    for interest in interest_list:
        if interest in ACTIVITY_TYPES:
            activities = random.sample(ACTIVITY_TYPES[interest], min(2, len(ACTIVITY_TYPES[interest])))
            suggestions.extend(activities)

    if not suggestions:
        suggestions = ["City Center Exploration", "Local Cafe Hopping", "Photography Walk"]

    result = f"Top Activities in {city} based on your interests ({interests}):\n\n"
    for i, activity in enumerate(suggestions[:5], 1):
        duration = random.choice(["2-3 hours", "Half day", "Full day"])
        price = random.choice(["Free", "€15-30", "€30-50", "€50+"])
        result += f"{i}. {activity}\n   Duration: {duration} | Price: {price}\n\n"

    return result


@tool
def plan_itinerary(city: str, days: int, style: str) -> str:
    """
    Create a day-by-day itinerary for a trip.

    Args:
        city: Destination city
        days: Number of days (1-7)
        style: Travel style (e.g., "relaxed", "packed", "balanced")

    Returns:
        Complete itinerary with daily plans
    """
    from demo_data.attractions import ATTRACTIONS

    # Get city attractions if available
    if city in ATTRACTIONS:
        city_attractions = ATTRACTIONS[city]
        morning_activities = [a["name"] for a in city_attractions if a["best_time"] in ["Morning", "Day trip"]]
        afternoon_activities = [a["name"] for a in city_attractions if a["best_time"] in ["Afternoon", "Day trip"]]
        evening_activities = [a["name"] for a in city_attractions if a["best_time"] in ["Evening", "Sunset"]]

        # Add generic options if not enough activities
        if len(morning_activities) < 3:
            morning_activities.extend(["Visit local market", "Museum tour", "Walking tour"])
        if len(afternoon_activities) < 3:
            afternoon_activities.extend(["Lunch at local restaurant", "Park relaxation", "Shopping district"])
        if len(evening_activities) < 3:
            evening_activities.extend(["Dinner at restaurant", "Rooftop bar", "Night walk"])
    else:
        # Generic activities for unknown cities
        morning_activities = ["Visit main attractions", "Explore old town", "Museum tour", "Market visit"]
        afternoon_activities = ["Lunch at local restaurant", "Shopping district", "Park relaxation", "Boat tour"]
        evening_activities = ["Dinner cruise", "Rooftop bar", "Theater show", "Night market"]

    itinerary = f"📅 {days}-Day Itinerary for {city} ({style} pace)\n\n"

    for day in range(1, min(days + 1, 8)):
        morning = random.choice(morning_activities)
        afternoon = random.choice(afternoon_activities)
        evening = random.choice(evening_activities)

        itinerary += (
            f"Day {day}:\n"
            f"  🌅 Morning: {morning}\n"
            f"  ☀️ Afternoon: {afternoon}\n"
            f"  🌙 Evening: {evening}\n\n"
        )

    return itinerary
