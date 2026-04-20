# Demo Data for Workshop

This folder contains **ready-to-use datasets** for building your custom agents. No need to create mock data from scratch!

## 🎯 How to Use

Simply import the data you need in your agent's tool:

```python
from demo_data.restaurants import RESTAURANTS
from demo_data.attractions import PHOTO_SPOTS
from demo_data.travel_info import USEFUL_PHRASES

@tool
def recommend_photo_spots(city: str) -> str:
    """Find the best photo spots in a city."""
    spots = PHOTO_SPOTS.get(city, ["City center", "Main square", "Waterfront"])
    return f"Top photo spots in {city}:\n" + "\n".join(f"📸 {spot}" for spot in spots)
```

## 📁 Available Datasets

### `flights.py`
- **AIRLINES** - List of airline names
- **FLIGHT_ROUTES** - Route data with durations and price ranges
- **DEPARTURE_TIMES** - Common departure times
- **FLIGHT_CLASSES** - Economy, business, first class multipliers
- **BOOKING_PREFIXES** - Booking reference prefixes

**Example use cases:**
- Flight search agent
- Price comparison tool
- Route planner

### `hotels.py`
- **HOTELS** - Hotel data by city with prices, ratings, amenities
- **ROOM_TYPE_PRICES** - Price multipliers for different room types
- **BOOKING_CONFIRMATION_PREFIXES** - Confirmation number prefixes

**Example use cases:**
- Hotel recommendation agent
- Accommodation finder
- Budget accommodation search

### `restaurants.py`
- **RESTAURANTS** - Restaurant data by city with details
- **CUISINES** - List of cuisine types
- **BUDGET_LEVELS** - Budget categories (€ to €€€€€)

**Example use cases:**
- Restaurant recommendation agent
- Food tour planner
- Budget dining finder

### `attractions.py`
- **ATTRACTIONS** - Tourist attractions by city with timing/pricing
- **ACTIVITY_TYPES** - Activities by category (adventure, cultural, etc.)
- **PHOTO_SPOTS** - Instagram-worthy locations

**Example use cases:**
- Itinerary builder
- Photo spot finder
- Activity recommender

### `travel_info.py`
- **VISA_REQUIREMENTS** - Visa info by country
- **LOCAL_CUSTOMS** - Cultural etiquette tips
- **USEFUL_PHRASES** - Common phrases in different languages
- **CURRENCY_INFO** - Currency details and tips
- **PACKING_ESSENTIALS** - What to pack by season
- **BUDGET_ESTIMATES** - Daily costs by travel style
- **SAFETY_TIPS** - General safety advice

**Example use cases:**
- Travel prep assistant
- Language phrasebook agent
- Budget calculator
- Visa checker
- Packing list generator

### `weather.py`
- **SEASONAL_WEATHER** - Weather by city and season
- **BEST_TIME_TO_VISIT** - Optimal travel periods
- **WEATHER_ACTIVITIES** - Activity suggestions by weather
- **MONTHLY_CONDITIONS** - Quick month reference

**Example use cases:**
- Weather advisor
- Best time to visit planner
- Activity suggester based on conditions

## 💡 Quick Examples

### Example 1: Simple Phrase Tool
```python
from demo_data.travel_info import USEFUL_PHRASES

@tool
def get_phrases(language: str) -> str:
    """Get useful phrases in a language."""
    phrases = USEFUL_PHRASES.get(language, {})
    if not phrases:
        return f"Phrases for {language} not available yet!"
    
    result = f"Useful {language} Phrases:\n\n"
    for english, translation in phrases.items():
        result += f"• {english}: {translation}\n"
    return result
```

### Example 2: Restaurant Finder
```python
from demo_data.restaurants import RESTAURANTS

@tool
def find_restaurants(city: str, budget: str) -> str:
    """Find restaurants in a city by budget."""
    city_restaurants = RESTAURANTS.get(city, RESTAURANTS["default"])
    
    result = f"Restaurants in {city} ({budget} budget):\n\n"
    for r in city_restaurants:
        if budget.lower() in r["price"].lower() or len(r["price"]) <= len(budget):
            result += f"🍽️ {r['name']}\n"
            result += f"   {r['cuisine']} • {r['price']} • ⭐ {r['rating']}/5\n"
            result += f"   Try: {', '.join(r['specialties'][:2])}\n\n"
    
    return result
```

### Example 3: Packing List
```python
from demo_data.travel_info import PACKING_ESSENTIALS

@tool
def create_packing_list(destination: str, season: str, days: int) -> str:
    """Create a packing list for a trip."""
    seasonal_items = PACKING_ESSENTIALS.get(season.lower(), [])
    always_items = PACKING_ESSENTIALS["always"]
    
    result = f"🎒 Packing List for {destination} ({days} days, {season})\n\n"
    result += "Essentials:\n"
    for item in always_items:
        result += f"☐ {item}\n"
    
    result += f"\n{season.title()} Specific:\n"
    for item in seasonal_items:
        result += f"☐ {item}\n"
    
    result += f"\nClothes: Pack {days} outfits (mix and match!)\n"
    return result
```

## 🎨 Tips for Using Demo Data

1. **Start simple** - Pick one dataset and build a basic tool
2. **Mix and match** - Combine multiple datasets for richer responses
3. **Add your twist** - Filter, format, or enhance the data in your tool
4. **Use fallbacks** - Many datasets have "default" entries for unknown cities
5. **Focus on Strands** - The data is ready, now focus on learning @tool, docstrings, and Agent()

## 🚀 Don't Overthink It!

The goal is to learn Strands SDK concepts:
- ✅ How to use `@tool` decorator
- ✅ How to write clear docstrings
- ✅ How to combine tools into an Agent
- ✅ How the orchestrator routes to your agent

The data is here so you can focus on **building agents**, not **creating datasets**!

## 🔧 Extending After the Workshop

Want to add real APIs later? These data structures show you exactly what information is useful:
- Replace `RESTAURANTS[city]` with Yelp API call
- Replace `SEASONAL_WEATHER[city]` with OpenWeather API
- Keep the same tool structure, just swap the data source!

---

**Happy building! 🎉**
