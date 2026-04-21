"""
Hotel booking tools - Mock implementations for workshop
"""
from strands import tool
import random

# Import demo data
from demo_data.hotels import HOTELS, DEFAULT_HOTELS


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
    # Get hotels from demo data
    city_hotels = HOTELS.get(city, DEFAULT_HOTELS)

    # Select 3 random hotels
    selected = random.sample(city_hotels, min(3, len(city_hotels)))

    hotels = []
    for i, hotel in enumerate(selected, 1):
        amenities = ", ".join(hotel["amenities"][:4])  # Show first 4 amenities

        hotels.append(
            f"Hotel {i}: {hotel['name']}\n"
            f"  Location: {hotel['location']}, {city}\n"
            f"  Rating: ⭐ {hotel['rating']}/5.0 | {'⭐' * hotel['stars']}\n"
            f"  Price: €{hotel['price_per_night']}/night\n"
            f"  Amenities: {amenities}\n"
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
    from demo_data.hotels import ROOM_TYPE_PRICES

    available_rooms = random.randint(2, 8)

    # Calculate price based on room type
    room_type_title = room_type.title()
    multiplier = ROOM_TYPE_PRICES.get(room_type_title, 1.0)
    base_price = int(150 * multiplier)  # Base standard room is €150

    return (
        f"Room Availability - {hotel_name}\n\n"
        f"Room Type: {room_type_title}\n"
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
    from demo_data.hotels import BOOKING_CONFIRMATION_PREFIXES

    prefix = random.choice(BOOKING_CONFIRMATION_PREFIXES)
    confirmation_number = f"{prefix}{random.randint(10000, 99999)}"

    return (
        f"🏨 Hotel Booked Successfully!\n\n"
        f"Confirmation Number: {confirmation_number}\n"
        f"Hotel: {hotel_name}\n"
        f"Room Type: {room_type.capitalize()}\n"
        f"Guest: {guest_name}\n"
        f"Confirmation sent to: {guest_email}\n\n"
        f"You can check in anytime after 3 PM on your arrival date."
    )
