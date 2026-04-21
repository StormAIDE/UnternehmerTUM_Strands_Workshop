"""
General travel information, tips, and practical data
"""

VISA_REQUIREMENTS = {
    "Germany": {
        "US": "No visa for stays up to 90 days",
        "UK": "No visa for stays up to 90 days",
        "India": "Schengen visa required",
        "China": "Schengen visa required",
        "Brazil": "No visa for stays up to 90 days",
    },
    "Japan": {
        "US": "No visa for stays up to 90 days",
        "UK": "No visa for stays up to 90 days",
        "India": "Visa required",
        "China": "Visa required (15-day exemption available)",
        "Brazil": "No visa for stays up to 90 days",
    },
    "Thailand": {
        "US": "30-day visa exemption",
        "UK": "30-day visa exemption",
        "India": "Visa on arrival available",
        "China": "Visa required",
        "Brazil": "30-day visa exemption",
    }
}

LOCAL_CUSTOMS = {
    "Japan": [
        "Remove shoes when entering homes and some restaurants",
        "Bow when greeting (slight nod is acceptable for foreigners)",
        "Don't tip - it can be considered rude",
        "Keep your voice down on public transport",
        "Avoid eating while walking"
    ],
    "Germany": [
        "Be punctual - Germans value timeliness",
        "Shake hands when meeting",
        "Separate your recycling properly",
        "Cash is still common - not all places accept cards",
        "Quiet hours: typically 10pm-6am and Sunday afternoons"
    ],
    "Thailand": [
        "Remove shoes before entering temples",
        "Don't touch anyone's head",
        "Feet are considered lowest - don't point them at people",
        "Dress modestly in temples",
        "The Thai Royal Family is highly respected - be respectful"
    ],
    "France": [
        "Greet shopkeepers when entering stores",
        "Say 'Bonjour' before asking questions",
        "Tipping is appreciated but not mandatory (5-10%)",
        "Dress well - French culture values appearance",
        "Don't rush meals - dining is an experience"
    ]
}

USEFUL_PHRASES = {
    "Japanese": {
        "Hello": "こんにちは (Konnichiwa)",
        "Thank you": "ありがとう (Arigatou)",
        "Excuse me": "すみません (Sumimasen)",
        "How much?": "いくらですか (Ikura desu ka)",
        "Help": "助けて (Tasukete)",
        "Delicious": "おいしい (Oishii)"
    },
    "German": {
        "Hello": "Hallo / Guten Tag",
        "Thank you": "Danke",
        "Excuse me": "Entschuldigung",
        "How much?": "Wie viel kostet das?",
        "Help": "Hilfe",
        "Cheers": "Prost"
    },
    "French": {
        "Hello": "Bonjour",
        "Thank you": "Merci",
        "Excuse me": "Excusez-moi",
        "How much?": "Combien ça coûte?",
        "Help": "Au secours",
        "Please": "S'il vous plaît"
    },
    "Spanish": {
        "Hello": "Hola",
        "Thank you": "Gracias",
        "Excuse me": "Disculpe",
        "How much?": "¿Cuánto cuesta?",
        "Help": "Ayuda",
        "Please": "Por favor"
    }
}

CURRENCY_INFO = {
    "Japan": {"currency": "Japanese Yen (¥)", "symbol": "¥", "code": "JPY", "tip": "Cash-heavy society, have yen on hand"},
    "Germany": {"currency": "Euro (€)", "symbol": "€", "code": "EUR", "tip": "Cards accepted but cash still common"},
    "Thailand": {"currency": "Thai Baht (฿)", "symbol": "฿", "code": "THB", "tip": "Carry small bills for markets and taxis"},
    "UK": {"currency": "British Pound (£)", "symbol": "£", "code": "GBP", "tip": "Cards widely accepted"},
    "USA": {"currency": "US Dollar ($)", "symbol": "$", "code": "USD", "tip": "Credit cards almost universal"},
    "France": {"currency": "Euro (€)", "symbol": "€", "code": "EUR", "tip": "Cards widely accepted, some small shops cash only"},
    "Spain": {"currency": "Euro (€)", "symbol": "€", "code": "EUR", "tip": "Cards accepted, small amounts may need cash"},
    "Italy": {"currency": "Euro (€)", "symbol": "€", "code": "EUR", "tip": "Cash preferred in small establishments"},
}

PACKING_ESSENTIALS = {
    "summer": ["Sunscreen", "Hat/Cap", "Sunglasses", "Light clothes", "Sandals", "Water bottle", "Swimsuit"],
    "winter": ["Warm jacket", "Gloves", "Scarf", "Thermal layers", "Warm boots", "Lip balm", "Hand warmers"],
    "spring": ["Light jacket", "Umbrella", "Layers", "Comfortable shoes", "Allergy medication"],
    "fall": ["Medium jacket", "Umbrella", "Layers", "Closed shoes", "Warm accessories"],
    "always": ["Passport", "Chargers", "Medications", "Travel insurance docs", "Credit cards", "Phone", "Adapter/converter"]
}

BUDGET_ESTIMATES = {
    "backpacker": {
        "accommodation": 25,
        "food": 15,
        "transport": 10,
        "activities": 10,
        "total_daily": 60
    },
    "budget": {
        "accommodation": 50,
        "food": 30,
        "transport": 15,
        "activities": 20,
        "total_daily": 115
    },
    "moderate": {
        "accommodation": 120,
        "food": 60,
        "transport": 25,
        "activities": 50,
        "total_daily": 255
    },
    "comfortable": {
        "accommodation": 200,
        "food": 100,
        "transport": 40,
        "activities": 80,
        "total_daily": 420
    },
    "luxury": {
        "accommodation": 400,
        "food": 200,
        "transport": 80,
        "activities": 150,
        "total_daily": 830
    }
}

TRANSPORTATION_TYPES = [
    "Metro/Subway",
    "Bus",
    "Tram",
    "Taxi/Ride-share",
    "Bike rental",
    "Walking",
    "Train",
    "Ferry",
    "Scooter rental"
]

SAFETY_TIPS = [
    "Keep copies of important documents",
    "Share your itinerary with someone at home",
    "Keep emergency contacts handy",
    "Be aware of common scams in the area",
    "Don't flash expensive items",
    "Use hotel safe for valuables",
    "Stay in well-lit areas at night",
    "Trust your instincts",
    "Have travel insurance",
    "Know the local emergency numbers"
]
