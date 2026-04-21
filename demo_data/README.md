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
    # The second argument is the fallback - customize it to anything you want!
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
- **VISA_REQUIREMENTS** - Visa info by country and nationality
- **LOCAL_CUSTOMS** - Cultural etiquette tips by country
- **USEFUL_PHRASES** - Common phrases in different languages
- **CURRENCY_INFO** - Currency details and payment tips (Japan, Germany, France, Spain, Italy, Thailand, UK, USA)
- **PACKING_ESSENTIALS** - What to pack by season
- **BUDGET_ESTIMATES** - Daily costs by travel style (backpacker to luxury)
- **SAFETY_TIPS** - General safety advice
- **TRANSPORTATION_TYPES** - Common transport modes

**Example use cases:**
- Travel prep assistant
- Language phrasebook agent
- Budget calculator
- Visa checker
- Packing list generator
- Currency advisor

### `destinations.py` ⭐ NEW
- **CITY_GUIDES** - Comprehensive guides for major cities (Paris, Tokyo, Barcelona, Munich, New York, London, Rome)
- **TRAVEL_TIPS** - Category-based tips (food, culture, nightlife, shopping, safety, photography)
- **CITY_NICKNAMES** - Quick lookup for common city abbreviations (NYC, LA, SF, etc.)

**Example use cases:**
- City guide agent
- Local tips advisor
- Destination information specialist
- Travel planning assistant

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

### Example 1: City Guide Tool (Using NEW destinations.py)
```python
from demo_data.destinations import CITY_GUIDES

@tool
def get_city_guide(city: str) -> str:
    """Get a comprehensive city guide."""
    # .get() with fallback: if city not found, use the "default" guide
    # You can customize this fallback to anything you want!
    guide = CITY_GUIDES.get(city.lower(), CITY_GUIDES["default"])
    
    return f"""City Guide: {city.title()}
    
🎯 Must-See: {guide['highlights']}
🌤️ Best Time: {guide['best_time']}
💡 Local Tip: {guide['local_tip']}
🚇 Transport: {guide['transport']}
"""
```

### Example 2: Simple Phrase Tool
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

### Example 3: Restaurant Finder
```python
from demo_data.restaurants import RESTAURANTS

@tool
def find_restaurants(city: str, budget: str) -> str:
    """Find restaurants in a city by budget."""
    # Using "default" key as fallback - another common pattern!
    city_restaurants = RESTAURANTS.get(city, RESTAURANTS["default"])
    
    result = f"Restaurants in {city} ({budget} budget):\n\n"
    for r in city_restaurants:
        if budget.lower() in r["price"].lower() or len(r["price"]) <= len(budget):
            result += f"🍽️ {r['name']}\n"
            result += f"   {r['cuisine']} • {r['price']} • ⭐ {r['rating']}/5\n"
            result += f"   Try: {', '.join(r['specialties'][:2])}\n\n"
    
    return result
```

### Example 4: Packing List
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

### 💡 Understanding the `.get()` Pattern

You'll see this pattern throughout the code:
```python
spots = PHOTO_SPOTS.get(city, ["City center", "Main square", "Waterfront"])
```

**How it works:**
- **First argument** (`city`) - The key to look up
- **Second argument** (`["City center", "Main square", "Waterfront"]`) - The **fallback/default value**

**Important:** The fallback is **completely customizable**! You can write anything you want:
```python
# ✅ Generic fallback
spots = PHOTO_SPOTS.get(city, ["City center", "Main square"])

# ✅ Helpful fallback
spots = PHOTO_SPOTS.get(city, ["Check online for popular spots"])

# ✅ Empty fallback
spots = PHOTO_SPOTS.get(city, [])

# ✅ Different data structure
guide = CITY_GUIDES.get(city.lower(), {
    "highlights": "Explore the city center",
    "best_time": "Spring or fall",
    "local_tip": "Ask locals for recommendations",
    "transport": "Use public transportation"
})
```

**When to use fallbacks:**
- ✅ When you want graceful handling of unknown cities
- ✅ When you want to provide generic advice
- ✅ When you want to encourage users to add their own data

**Examples from existing code:**
```python
# Flight tools
route_info = FLIGHT_ROUTES.get(route_key, DEFAULT_ROUTE)  # Uses a predefined constant

# Hotel tools  
city_hotels = HOTELS.get(city, DEFAULT_HOTELS)  # Uses a predefined list

# Restaurant tools
city_restaurants = RESTAURANTS.get(city, RESTAURANTS["default"])  # Uses the "default" key

# Your custom fallback
custom_data = MY_DATA.get(city, "Sorry, no data available for this city")  # Simple string
```

**Pro tip:** Look at existing tools to see different fallback patterns, then choose what makes sense for your agent!

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
