"""
Weather and itinerary tools - Mock implementations
"""
from strands import tool
import random


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
    conditions = ["Sunny", "Partly Cloudy", "Cloudy", "Light Rain", "Clear"]
    condition = random.choice(conditions)
    temp_high = random.randint(18, 32)
    temp_low = temp_high - random.randint(5, 10)
    humidity = random.randint(40, 80)

    return (
        f"Weather Forecast for {city}\n"
        f"Date: {date}\n\n"
        f"Condition: {condition}\n"
        f"Temperature: {temp_low}°C - {temp_high}°C\n"
        f"Humidity: {humidity}%\n"
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
    activities_db = {
        "culture": ["Visit Historic Museum", "Old Town Walking Tour", "Art Gallery Visit"],
        "food": ["Food Market Tour", "Cooking Class", "Restaurant Crawl"],
        "nature": ["City Park Picnic", "Botanical Garden", "River Cruise"],
        "adventure": ["Bike Tour", "Rock Climbing", "Water Sports"],
        "shopping": ["Local Markets", "Shopping District", "Artisan Shops"]
    }

    interest_list = [i.strip().lower() for i in interests.split(",")]
    suggestions = []

    for interest in interest_list:
        if interest in activities_db:
            activities = random.sample(activities_db[interest], min(2, len(activities_db[interest])))
            suggestions.extend(activities)

    if not suggestions:
        suggestions = ["City Center Exploration", "Local Cafe Hopping", "Photography Walk"]

    result = f"Top Activities in {city}:\n\n"
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
