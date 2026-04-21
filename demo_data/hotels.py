"""
Hotel data for building hotel booking agents
"""

HOTELS = {
    "Paris": [
        {
            "name": "Grand Hotel Central",
            "stars": 5,
            "price_per_night": 320,
            "rating": 4.8,
            "location": "City Center",
            "amenities": ["WiFi", "Breakfast", "Pool", "Spa", "Gym", "Restaurant"],
            "room_types": ["Standard", "Deluxe", "Suite"]
        },
        {
            "name": "Riverside Luxury Suites",
            "stars": 4,
            "price_per_night": 210,
            "rating": 4.6,
            "location": "Near Seine River",
            "amenities": ["WiFi", "Breakfast", "Gym", "Bar"],
            "room_types": ["Standard", "Deluxe"]
        },
        {
            "name": "Urban Boutique Hotel",
            "stars": 4,
            "price_per_night": 180,
            "rating": 4.5,
            "location": "Latin Quarter",
            "amenities": ["WiFi", "Breakfast", "Rooftop Terrace"],
            "room_types": ["Standard", "Superior"]
        },
        {
            "name": "Budget Stay Paris",
            "stars": 3,
            "price_per_night": 95,
            "rating": 4.2,
            "location": "Near Metro",
            "amenities": ["WiFi", "24h Reception"],
            "room_types": ["Standard"]
        }
    ],
    "Tokyo": [
        {
            "name": "Tokyo Imperial Hotel",
            "stars": 5,
            "price_per_night": 380,
            "rating": 4.9,
            "location": "Shibuya",
            "amenities": ["WiFi", "Breakfast", "Pool", "Spa", "Gym", "Multiple Restaurants"],
            "room_types": ["Standard", "Deluxe", "Suite", "Executive"]
        },
        {
            "name": "Sakura Business Hotel",
            "stars": 3,
            "price_per_night": 120,
            "rating": 4.4,
            "location": "Shinjuku",
            "amenities": ["WiFi", "Breakfast", "Gym"],
            "room_types": ["Standard", "Superior"]
        },
        {
            "name": "Capsule Hotel Tokyo",
            "stars": 2,
            "price_per_night": 45,
            "rating": 4.0,
            "location": "Akihabara",
            "amenities": ["WiFi", "Shared Bath", "Lounge"],
            "room_types": ["Capsule"]
        }
    ],
    "Munich": [
        {
            "name": "Bavarian Palace Hotel",
            "stars": 5,
            "price_per_night": 295,
            "rating": 4.7,
            "location": "Marienplatz",
            "amenities": ["WiFi", "Breakfast", "Spa", "Restaurant", "Bar"],
            "room_types": ["Standard", "Deluxe", "Suite"]
        },
        {
            "name": "Munich Central Inn",
            "stars": 3,
            "price_per_night": 110,
            "rating": 4.3,
            "location": "Near Train Station",
            "amenities": ["WiFi", "Breakfast"],
            "room_types": ["Standard", "Family Room"]
        },
        {
            "name": "Hostel Bavaria",
            "stars": 2,
            "price_per_night": 35,
            "rating": 4.1,
            "location": "Near English Garden",
            "amenities": ["WiFi", "Shared Kitchen", "Common Room"],
            "room_types": ["Dorm", "Private Room"]
        }
    ],
    "Barcelona": [
        {
            "name": "Seaside Resort & Spa",
            "stars": 5,
            "price_per_night": 340,
            "rating": 4.8,
            "location": "Barceloneta Beach",
            "amenities": ["WiFi", "Breakfast", "Pool", "Spa", "Beach Access", "Restaurant"],
            "room_types": ["Standard", "Deluxe", "Suite", "Oceanview"]
        },
        {
            "name": "Gothic Quarter Boutique",
            "stars": 4,
            "price_per_night": 165,
            "rating": 4.6,
            "location": "Gothic Quarter",
            "amenities": ["WiFi", "Breakfast", "Rooftop Terrace"],
            "room_types": ["Standard", "Superior"]
        },
        {
            "name": "Barcelona Budget Stay",
            "stars": 3,
            "price_per_night": 80,
            "rating": 4.2,
            "location": "Near Metro",
            "amenities": ["WiFi", "24h Reception"],
            "room_types": ["Standard"]
        }
    ],
    "New York": [
        {
            "name": "Manhattan Grand Hotel",
            "stars": 5,
            "price_per_night": 450,
            "rating": 4.8,
            "location": "Midtown Manhattan",
            "amenities": ["WiFi", "Gym", "Restaurant", "Bar", "Concierge"],
            "room_types": ["Standard", "Deluxe", "Suite", "Penthouse"]
        },
        {
            "name": "Brooklyn Modern Inn",
            "stars": 3,
            "price_per_night": 140,
            "rating": 4.4,
            "location": "Brooklyn",
            "amenities": ["WiFi", "Breakfast", "Cafe"],
            "room_types": ["Standard", "Queen", "King"]
        }
    ],
}

# Default hotels for unknown cities
DEFAULT_HOTELS = [
    {
        "name": "City Center Hotel",
        "stars": 4,
        "price_per_night": 150,
        "rating": 4.4,
        "location": "City Center",
        "amenities": ["WiFi", "Breakfast", "Gym"],
        "room_types": ["Standard", "Deluxe"]
    },
    {
        "name": "Budget Accommodation",
        "stars": 3,
        "price_per_night": 75,
        "rating": 4.1,
        "location": "Near Public Transport",
        "amenities": ["WiFi", "24h Reception"],
        "room_types": ["Standard"]
    },
    {
        "name": "Luxury Resort",
        "stars": 5,
        "price_per_night": 350,
        "rating": 4.7,
        "location": "Premium Location",
        "amenities": ["WiFi", "Breakfast", "Pool", "Spa", "Gym", "Restaurant"],
        "room_types": ["Standard", "Deluxe", "Suite"]
    }
]

ROOM_TYPE_PRICES = {
    "Standard": 1.0,
    "Superior": 1.3,
    "Deluxe": 1.6,
    "Suite": 2.5,
    "Executive": 2.0,
    "Family Room": 1.8,
    "Oceanview": 1.7,
    "Penthouse": 4.0,
    "Capsule": 0.4,
    "Dorm": 0.3,
    "Private Room": 0.8,
    "Queen": 1.1,
    "King": 1.2
}

BOOKING_CONFIRMATION_PREFIXES = ["HTL", "RES", "BOOK", "STAY"]
