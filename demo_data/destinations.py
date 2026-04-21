"""
Destination guides and city information data
"""

CITY_GUIDES = {
    "paris": {
        "highlights": "Eiffel Tower, Louvre, Notre-Dame, Champs-Élysées",
        "best_time": "April-June, September-October",
        "local_tip": "Buy museum passes in advance to skip lines",
        "transport": "Metro is efficient and covers all major areas"
    },
    "tokyo": {
        "highlights": "Senso-ji Temple, Shibuya Crossing, Tokyo Tower, Tsukiji Market",
        "best_time": "March-May (cherry blossoms), October-November",
        "local_tip": "Get a Suica card for easy public transport",
        "transport": "Subway and JR lines are the best way to get around"
    },
    "barcelona": {
        "highlights": "Sagrada Familia, Park Güell, La Rambla, Gothic Quarter",
        "best_time": "May-June, September-October",
        "local_tip": "Book Gaudí attractions online to avoid long waits",
        "transport": "Metro and walking are perfect for exploring"
    },
    "munich": {
        "highlights": "Marienplatz, English Garden, Neuschwanstein Castle, BMW Museum",
        "best_time": "May-September (summer), September-October (Oktoberfest)",
        "local_tip": "Get a Bayern pass for unlimited regional train travel",
        "transport": "U-Bahn and S-Bahn cover the entire city efficiently"
    },
    "new york": {
        "highlights": "Statue of Liberty, Central Park, Times Square, Brooklyn Bridge",
        "best_time": "April-June, September-November",
        "local_tip": "Get a MetroCard and explore neighborhoods beyond Manhattan",
        "transport": "Subway runs 24/7 and reaches all boroughs"
    },
    "london": {
        "highlights": "Big Ben, British Museum, Tower of London, Buckingham Palace",
        "best_time": "May-September (warmest weather)",
        "local_tip": "Get an Oyster card for cheaper tube and bus fares",
        "transport": "Underground (tube) is the fastest way around"
    },
    "rome": {
        "highlights": "Colosseum, Vatican City, Trevi Fountain, Roman Forum",
        "best_time": "April-May, September-October",
        "local_tip": "Book Vatican tickets online and visit early morning",
        "transport": "Metro covers main sites, but walking is best in center"
    },
    "default": {
        "highlights": "Historic center, local markets, museums, parks",
        "best_time": "Spring and fall typically offer great weather",
        "local_tip": "Ask locals for hidden gem recommendations",
        "transport": "Use public transport or walking tours"
    }
}

TRAVEL_TIPS = {
    "food": [
        "Try local street food markets for authentic cuisine",
        "Visit during lunch hours for better deals at restaurants",
        "Ask locals for their favorite neighborhood spots",
        "Don't skip the local breakfast specialties"
    ],
    "culture": [
        "Many museums offer free entry on certain days",
        "Join free walking tours to learn city history",
        "Check local event calendars for festivals",
        "Visit neighborhoods beyond the tourist center"
    ],
    "nightlife": [
        "Local bars often have happy hour deals",
        "Ask your hotel for safe nightlife areas",
        "Use official taxi or rideshare apps",
        "Clubs typically get busy after midnight"
    ],
    "shopping": [
        "Local markets offer better prices than tourist shops",
        "Negotiate at markets but be respectful",
        "Keep receipts for potential tax refunds",
        "Shop in local neighborhoods for unique finds"
    ],
    "safety": [
        "Keep valuables in hotel safe",
        "Be aware of common tourist scams",
        "Use registered taxis or rideshare apps",
        "Keep copies of important documents"
    ],
    "photography": [
        "Visit popular spots early morning for fewer crowds",
        "Golden hour (sunrise/sunset) provides best lighting",
        "Ask permission before photographing locals",
        "Research the best viewpoints in advance"
    ]
}

# Quick reference for popular cities
CITY_NICKNAMES = {
    "nyc": "new york",
    "ny": "new york",
    "la": "los angeles",
    "sf": "san francisco",
    "vegas": "las vegas",
    "dc": "washington",
}
