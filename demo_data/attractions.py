"""
Tourist attractions and activities data
"""

ATTRACTIONS = {
    "Paris": [
        {"name": "Eiffel Tower", "type": "landmark", "duration": "2-3 hours", "price": "€€", "best_time": "Sunset"},
        {"name": "Louvre Museum", "type": "museum", "duration": "3-4 hours", "price": "€€", "best_time": "Morning"},
        {"name": "Notre-Dame Cathedral", "type": "historic", "duration": "1 hour", "price": "Free", "best_time": "Afternoon"},
        {"name": "Seine River Cruise", "type": "activity", "duration": "1 hour", "price": "€€", "best_time": "Evening"},
        {"name": "Montmartre & Sacré-Cœur", "type": "neighborhood", "duration": "2-3 hours", "price": "Free", "best_time": "Morning"},
    ],
    "Tokyo": [
        {"name": "Senso-ji Temple", "type": "historic", "duration": "1-2 hours", "price": "Free", "best_time": "Morning"},
        {"name": "Shibuya Crossing", "type": "landmark", "duration": "30 mins", "price": "Free", "best_time": "Evening"},
        {"name": "Tokyo Skytree", "type": "observation", "duration": "2 hours", "price": "€€€", "best_time": "Sunset"},
        {"name": "Tsukiji Fish Market", "type": "market", "duration": "2 hours", "price": "€", "best_time": "Early Morning"},
        {"name": "Meiji Shrine", "type": "historic", "duration": "1 hour", "price": "Free", "best_time": "Morning"},
    ],
    "Munich": [
        {"name": "Marienplatz", "type": "landmark", "duration": "1 hour", "price": "Free", "best_time": "11am (Glockenspiel)"},
        {"name": "English Garden", "type": "park", "duration": "2-3 hours", "price": "Free", "best_time": "Afternoon"},
        {"name": "Neuschwanstein Castle", "type": "historic", "duration": "Full day", "price": "€€€", "best_time": "Day trip"},
        {"name": "BMW Museum", "type": "museum", "duration": "2 hours", "price": "€€", "best_time": "Afternoon"},
        {"name": "Viktualienmarkt", "type": "market", "duration": "1-2 hours", "price": "€", "best_time": "Morning"},
    ],
    "Barcelona": [
        {"name": "Sagrada Família", "type": "landmark", "duration": "2 hours", "price": "€€€", "best_time": "Morning"},
        {"name": "Park Güell", "type": "park", "duration": "2-3 hours", "price": "€€", "best_time": "Afternoon"},
        {"name": "Las Ramblas", "type": "street", "duration": "1 hour", "price": "Free", "best_time": "Evening"},
        {"name": "Gothic Quarter", "type": "neighborhood", "duration": "2 hours", "price": "Free", "best_time": "Afternoon"},
        {"name": "Beach Barceloneta", "type": "beach", "duration": "3-4 hours", "price": "Free", "best_time": "Afternoon"},
    ],
    "New York": [
        {"name": "Statue of Liberty", "type": "landmark", "duration": "3-4 hours", "price": "€€€", "best_time": "Morning"},
        {"name": "Central Park", "type": "park", "duration": "2-3 hours", "price": "Free", "best_time": "Afternoon"},
        {"name": "Times Square", "type": "landmark", "duration": "1 hour", "price": "Free", "best_time": "Evening"},
        {"name": "Metropolitan Museum", "type": "museum", "duration": "3-4 hours", "price": "€€€", "best_time": "Morning"},
        {"name": "Brooklyn Bridge Walk", "type": "activity", "duration": "1 hour", "price": "Free", "best_time": "Sunset"},
    ],
}

ACTIVITY_TYPES = {
    "adventure": ["Hiking", "Rock Climbing", "Kayaking", "Zip-lining", "Paragliding"],
    "cultural": ["Museum Tour", "Historic Walk", "Cooking Class", "Language Exchange", "Traditional Performance"],
    "relaxation": ["Spa Day", "Beach Time", "Yoga Session", "Hot Springs", "Meditation Retreat"],
    "nightlife": ["Rooftop Bar", "Live Music Venue", "Night Market", "Club Tour", "Comedy Show"],
    "food": ["Food Tour", "Wine Tasting", "Cooking Workshop", "Market Visit", "Street Food Walk"],
    "nature": ["Park Visit", "Botanical Garden", "Wildlife Watching", "Scenic Drive", "River Cruise"],
}

PHOTO_SPOTS = {
    "Paris": ["Eiffel Tower from Trocadéro", "Louvre Pyramid", "Arc de Triomphe", "Sacré-Cœur Steps", "Pont Alexandre III"],
    "Tokyo": ["Shibuya Crossing from above", "Tokyo Tower at night", "Cherry blossoms in Ueno Park", "Senso-ji Temple gate", "Shinjuku neon lights"],
    "Munich": ["Marienplatz with City Hall", "English Garden Chinese Tower", "Neuschwanstein Castle", "Olympic Park Tower view", "Isar River sunset"],
    "Barcelona": ["Sagrada Família towers", "Park Güell mosaic bench", "Gothic Quarter alleyways", "Beach sunrise", "Casa Batlló facade"],
    "New York": ["Brooklyn Bridge at sunrise", "Top of the Rock view", "Central Park Bow Bridge", "Times Square lights", "DUMBO waterfront"],
}
