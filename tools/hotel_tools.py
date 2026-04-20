"""
Hotel booking tools - Mock implementations for workshop
"""
from strands import tool
import random


@tool
def find_hotels(city: str, checkin_date: str, checkout_date: str, guests: int = 2) -> str:
    """
    Find available hotels in a city.

    Args:
        city: City name (e.g., "Paris", "Tokyo")
        checkin_date: Check-in date (YYYY-MM-DD)
        checkout_date: Check-out date (YYYY-MM-DD)
        guests: Number of guests (default: 2)

    Returns:
        List of available hotels with details
    """
    hotel_names = [
        "Grand Hotel Central", "Riverside Luxury Suites", "Urban Boutique Hotel",
        "Seaside Resort & Spa", "Historic Palace Hotel"
    ]

    hotels = []
    for i in range(3):
        name = random.choice(hotel_names)
        rating = round(random.uniform(4.0, 4.9), 1)
        price_per_night = random.randint(80, 350)

        hotels.append(
            f"Hotel {i+1}: {name}\n"
            f"  Location: {city} City Center\n"
            f"  Rating: ⭐ {rating}/5.0\n"
            f"  Price: €{price_per_night}/night\n"
            f"  Amenities: WiFi, Breakfast, Pool, Gym\n"
        )

    return "\n".join(hotels)


@tool
def check_rooms(hotel_name: str, room_type: str) -> str:
    """
    Check room availability and details.

    Args:
        hotel_name: Name of the hotel
        room_type: Type of room (e.g., "standard", "deluxe", "suite")

    Returns:
        Room availability and pricing
    """
    available_rooms = random.randint(2, 8)
    base_price = 120 if room_type == "standard" else 200 if room_type == "deluxe" else 350

    return (
        f"Room Availability - {hotel_name}\n\n"
        f"Room Type: {room_type.capitalize()}\n"
        f"Available Rooms: {available_rooms}\n"
        f"Price: €{base_price}/night\n"
        f"Max Occupancy: 2-3 guests\n"
        f"View: City/Garden view\n"
        f"Cancellation: Free up to 24h before check-in"
    )


@tool
def book_hotel(hotel_name: str, room_type: str, guest_name: str, guest_email: str) -> str:
    """
    Book a hotel room.

    Args:
        hotel_name: Name of the hotel
        room_type: Type of room
        guest_name: Guest full name
        guest_email: Guest email for confirmation

    Returns:
        Booking confirmation
    """
    confirmation_number = f"HTL{random.randint(10000, 99999)}"

    return (
        f"🏨 Hotel Booked Successfully!\n\n"
        f"Confirmation Number: {confirmation_number}\n"
        f"Hotel: {hotel_name}\n"
        f"Room Type: {room_type.capitalize()}\n"
        f"Guest: {guest_name}\n"
        f"Confirmation sent to: {guest_email}\n\n"
        f"You can check in anytime after 3 PM on your arrival date."
    )
