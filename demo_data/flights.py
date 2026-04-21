"""
Flight data for building flight booking agents
"""

AIRLINES = [
    "Lufthansa",
    "Emirates",
    "British Airways",
    "Air France",
    "Singapore Airlines",
    "United Airlines",
    "Delta",
    "KLM",
    "Qatar Airways",
    "Turkish Airlines"
]

# Sample flight routes with typical prices and durations
FLIGHT_ROUTES = {
    ("Munich", "Tokyo"): {"duration": "11-12h", "price_range": (800, 1400)},
    ("Munich", "Paris"): {"duration": "1.5-2h", "price_range": (120, 350)},
    ("Munich", "London"): {"duration": "2h", "price_range": (150, 400)},
    ("Munich", "New York"): {"duration": "9-10h", "price_range": (500, 1200)},
    ("Munich", "Barcelona"): {"duration": "2-2.5h", "price_range": (100, 300)},

    ("Paris", "Tokyo"): {"duration": "12-13h", "price_range": (900, 1500)},
    ("Paris", "New York"): {"duration": "8-9h", "price_range": (450, 1100)},
    ("Paris", "Barcelona"): {"duration": "2h", "price_range": (80, 250)},
    ("Paris", "London"): {"duration": "1.5h", "price_range": (100, 300)},

    ("London", "New York"): {"duration": "7-8h", "price_range": (400, 1000)},
    ("London", "Tokyo"): {"duration": "12-13h", "price_range": (850, 1450)},
    ("London", "Barcelona"): {"duration": "2-2.5h", "price_range": (90, 280)},

    ("Frankfurt", "New York"): {"duration": "8-9h", "price_range": (480, 1100)},
    ("Frankfurt", "Tokyo"): {"duration": "11-12h", "price_range": (820, 1380)},
    ("Frankfurt", "London"): {"duration": "1.5h", "price_range": (140, 380)},

    ("Berlin", "Tokyo"): {"duration": "11-12h", "price_range": (850, 1420)},
    ("Berlin", "Barcelona"): {"duration": "2.5-3h", "price_range": (110, 320)},
    ("Berlin", "Paris"): {"duration": "2h", "price_range": (130, 360)},
}

# Default route info for unknown routes
DEFAULT_ROUTE = {"duration": "5-8h", "price_range": (400, 1000)}

DEPARTURE_TIMES = [
    "06:00", "07:30", "09:15", "10:45",
    "12:30", "14:00", "16:20", "18:45",
    "20:15", "22:00"
]

FLIGHT_CLASSES = {
    "economy": {"multiplier": 1.0, "label": "Economy"},
    "premium": {"multiplier": 1.5, "label": "Premium Economy"},
    "business": {"multiplier": 3.0, "label": "Business Class"},
    "first": {"multiplier": 5.0, "label": "First Class"}
}

# Sample booking references for mock bookings
BOOKING_PREFIXES = ["BK", "FL", "AIR", "TIX"]
