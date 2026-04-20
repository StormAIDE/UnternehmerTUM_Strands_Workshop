"""
Weather-related data for travel planning
"""

# Typical weather patterns by city and season
SEASONAL_WEATHER = {
    "Paris": {
        "spring": {"temp_range": "10-18°C", "conditions": "Mild, occasional rain", "clothing": "Light jacket, layers"},
        "summer": {"temp_range": "20-25°C", "conditions": "Warm, sunny", "clothing": "Light clothes, sunscreen"},
        "fall": {"temp_range": "10-16°C", "conditions": "Cool, rainy", "clothing": "Jacket, umbrella"},
        "winter": {"temp_range": "3-8°C", "conditions": "Cold, occasional snow", "clothing": "Warm coat, layers"}
    },
    "Tokyo": {
        "spring": {"temp_range": "15-20°C", "conditions": "Pleasant, cherry blossoms", "clothing": "Light layers"},
        "summer": {"temp_range": "26-32°C", "conditions": "Hot, humid, rainy season", "clothing": "Light breathable clothes"},
        "fall": {"temp_range": "15-22°C", "conditions": "Mild, beautiful foliage", "clothing": "Light jacket"},
        "winter": {"temp_range": "5-12°C", "conditions": "Cold, dry, sunny", "clothing": "Warm coat"}
    },
    "Munich": {
        "spring": {"temp_range": "8-18°C", "conditions": "Variable, occasional rain", "clothing": "Layers, light jacket"},
        "summer": {"temp_range": "18-24°C", "conditions": "Warm, occasional storms", "clothing": "Light clothes, jacket for evenings"},
        "fall": {"temp_range": "7-15°C", "conditions": "Cool, colorful leaves", "clothing": "Warm layers"},
        "winter": {"temp_range": "-2-5°C", "conditions": "Cold, snow likely", "clothing": "Heavy winter coat, boots"}
    },
    "Barcelona": {
        "spring": {"temp_range": "15-20°C", "conditions": "Pleasant, sunny", "clothing": "Light layers"},
        "summer": {"temp_range": "25-30°C", "conditions": "Hot, beach weather", "clothing": "Summer clothes, swimsuit"},
        "fall": {"temp_range": "18-24°C", "conditions": "Warm, ideal weather", "clothing": "Light clothes, light jacket"},
        "winter": {"temp_range": "10-15°C", "conditions": "Mild, some rain", "clothing": "Light jacket, layers"}
    },
    "New York": {
        "spring": {"temp_range": "10-20°C", "conditions": "Variable, warming up", "clothing": "Layers, light jacket"},
        "summer": {"temp_range": "25-32°C", "conditions": "Hot, humid", "clothing": "Light breathable clothes"},
        "fall": {"temp_range": "10-20°C", "conditions": "Crisp, colorful", "clothing": "Jacket, layers"},
        "winter": {"temp_range": "-5-5°C", "conditions": "Cold, snow possible", "clothing": "Heavy winter coat, boots"}
    }
}

BEST_TIME_TO_VISIT = {
    "Paris": {
        "best": ["April-June", "September-October"],
        "avoid": ["August (crowded, hot)", "January (very cold)"],
        "reason": "Spring and fall offer pleasant weather and fewer crowds"
    },
    "Tokyo": {
        "best": ["March-May (cherry blossoms)", "October-November (fall colors)"],
        "avoid": ["July-August (very hot and humid)", "June (rainy season)"],
        "reason": "Spring and fall have ideal weather and beautiful scenery"
    },
    "Munich": {
        "best": ["May-September", "December (Christmas markets)"],
        "avoid": ["January-February (very cold)"],
        "reason": "Summer for outdoor activities, winter for festive atmosphere"
    },
    "Barcelona": {
        "best": ["May-June", "September-October"],
        "avoid": ["August (extremely hot and crowded)"],
        "reason": "Late spring and early fall offer perfect beach weather without peak crowds"
    },
    "Thailand": {
        "best": ["November-February"],
        "avoid": ["April-May (very hot)", "September-October (heavy rain)"],
        "reason": "Cool and dry season is most comfortable"
    }
}

WEATHER_ACTIVITIES = {
    "sunny": [
        "Beach day",
        "Outdoor sightseeing",
        "Park picnic",
        "Walking tour",
        "Rooftop bar",
        "Bike rental",
        "Outdoor dining"
    ],
    "rainy": [
        "Museum visit",
        "Indoor market",
        "Cafe hopping",
        "Spa day",
        "Shopping mall",
        "Cooking class",
        "Theater show"
    ],
    "cold": [
        "Hot chocolate at cafe",
        "Indoor attractions",
        "Christmas markets",
        "Cozy restaurant",
        "Museum tour",
        "Thermal baths",
        "Indoor sports"
    ],
    "hot": [
        "Beach/pool time",
        "Air-conditioned museums",
        "Ice cream tasting",
        "Early morning activities",
        "Evening strolls",
        "Water sports",
        "Shaded parks"
    ]
}

# Month-by-month quick reference
MONTHLY_CONDITIONS = {
    1: "Winter - cold in most northern destinations",
    2: "Late winter - still cold, start planning spring trips",
    3: "Early spring - warming up, good for Japan cherry blossoms",
    4: "Spring - ideal for Europe, pleasant weather",
    5: "Late spring - great for most destinations, pre-summer",
    6: "Early summer - warm, good for beach destinations",
    7: "Summer - peak season, hot in most places",
    8: "Late summer - hottest month, very crowded",
    9: "Early fall - excellent weather, fewer crowds",
    10: "Fall - beautiful colors, comfortable temperatures",
    11: "Late fall - cooler, start of off-season deals",
    12: "Winter - cold, but festive (Christmas markets)"
}
