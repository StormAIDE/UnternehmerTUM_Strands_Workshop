"""
Restaurant data for building restaurant recommendation agents
"""

RESTAURANTS = {
    "Paris": [
        {
            "name": "Le Petit Bistro",
            "cuisine": "French",
            "price": "€€€",
            "rating": 4.7,
            "specialties": ["Coq au Vin", "Escargot", "Crème Brûlée"],
            "atmosphere": "Romantic, candlelit"
        },
        {
            "name": "Sakura Sushi",
            "cuisine": "Japanese",
            "price": "€€",
            "rating": 4.5,
            "specialties": ["Fresh Sashimi", "Dragon Roll", "Miso Soup"],
            "atmosphere": "Modern, minimalist"
        },
        {
            "name": "Mama Rosa's",
            "cuisine": "Italian",
            "price": "€€",
            "rating": 4.6,
            "specialties": ["Handmade Pasta", "Pizza Margherita", "Tiramisu"],
            "atmosphere": "Cozy, family-friendly"
        },
        {
            "name": "Street Food Market",
            "cuisine": "International",
            "price": "€",
            "rating": 4.3,
            "specialties": ["Tacos", "Falafel", "Pad Thai"],
            "atmosphere": "Casual, vibrant"
        }
    ],
    "Tokyo": [
        {
            "name": "Ichiran Ramen",
            "cuisine": "Japanese",
            "price": "€",
            "rating": 4.8,
            "specialties": ["Tonkotsu Ramen", "Gyoza"],
            "atmosphere": "Solo dining booths"
        },
        {
            "name": "Sukiyabashi Jiro",
            "cuisine": "Japanese",
            "price": "€€€€€",
            "rating": 4.9,
            "specialties": ["Omakase Sushi", "Seasonal Fish"],
            "atmosphere": "Exclusive, traditional"
        },
        {
            "name": "Gyukatsu Motomura",
            "cuisine": "Japanese",
            "price": "€€",
            "rating": 4.7,
            "specialties": ["Beef Cutlet", "Wasabi Set"],
            "atmosphere": "Quick service, local favorite"
        }
    ],
    "Munich": [
        {
            "name": "Hofbräuhaus",
            "cuisine": "German",
            "price": "€€",
            "rating": 4.4,
            "specialties": ["Schweinshaxe", "Weisswurst", "Pretzels"],
            "atmosphere": "Traditional beer hall"
        },
        {
            "name": "Tantris",
            "cuisine": "Fine Dining",
            "price": "€€€€€",
            "rating": 4.9,
            "specialties": ["Tasting Menu", "Wine Pairing"],
            "atmosphere": "Michelin-starred elegance"
        },
        {
            "name": "Viktualienmarkt Stalls",
            "cuisine": "German",
            "price": "€",
            "rating": 4.5,
            "specialties": ["Bratwurst", "Fresh Produce", "Local Cheese"],
            "atmosphere": "Open-air market"
        }
    ],
    # Generic fallback for any other city
    "default": [
        {
            "name": "Local Favorite Bistro",
            "cuisine": "Local",
            "price": "€€",
            "rating": 4.4,
            "specialties": ["Regional Specialties", "Seasonal Menu"],
            "atmosphere": "Authentic local experience"
        },
        {
            "name": "International Food Court",
            "cuisine": "International",
            "price": "€",
            "rating": 4.2,
            "specialties": ["Various cuisines", "Quick bites"],
            "atmosphere": "Casual dining"
        },
        {
            "name": "Fine Dining Restaurant",
            "cuisine": "Contemporary",
            "price": "€€€€",
            "rating": 4.7,
            "specialties": ["Chef's Tasting Menu", "Wine Selection"],
            "atmosphere": "Upscale, elegant"
        }
    ]
}

# Cuisine types for filtering
CUISINES = [
    "French", "Italian", "Japanese", "Chinese", "Mexican",
    "Indian", "Thai", "German", "American", "Mediterranean",
    "Korean", "Vietnamese", "Spanish", "Greek", "Turkish"
]

# Budget categories
BUDGET_LEVELS = {
    "budget": "€",
    "moderate": "€€",
    "mid-range": "€€€",
    "upscale": "€€€€",
    "luxury": "€€€€€"
}
