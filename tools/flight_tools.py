"""
Flight booking tools - Mock implementations for workshop
In production, these would connect to real flight APIs
"""
from strands import tool
import random

# Import demo data
from demo_data.flights import AIRLINES, FLIGHT_ROUTES, DEFAULT_ROUTE, DEPARTURE_TIMES


@tool
def search_flights(origin: str, destination: str, date: str) -> str:
    """
    Search for available flights between two cities.

    Args:
        origin: Departure city (e.g., "Munich", "NYC")
        destination: Arrival city (e.g., "Tokyo", "Paris")
        date: Travel date in YYYY-MM-DD format

    Returns:
        String with available flight options
    """
    # Get route info from demo data
    route_key = (origin, destination)
    reverse_route_key = (destination, origin)

    route_info = FLIGHT_ROUTES.get(route_key) or FLIGHT_ROUTES.get(reverse_route_key) or DEFAULT_ROUTE

    duration = route_info["duration"]
    price_min, price_max = route_info["price_range"]

    flights = []
    for i in range(3):
        airline = random.choice(AIRLINES)
        price = random.randint(price_min, price_max)
        departure = random.choice(DEPARTURE_TIMES)

        flights.append(
            f"Flight {i+1}: {airline}\n"
            f"  Route: {origin} → {destination}\n"
            f"  Date: {date}\n"
            f"  Departure: {departure}\n"
            f"  Duration: {duration}\n"
            f"  Price: €{price}\n"
        )

    return "\n".join(flights)


@tool
def book_flight(flight_id: str, passenger_name: str, passenger_email: str) -> str:
    """
    Book a flight for a passenger.

    Args:
        flight_id: Flight identifier (e.g., "LH123")
        passenger_name: Full name of passenger
        passenger_email: Email address for confirmation

    Returns:
        Booking confirmation details
    """
    from demo_data.flights import BOOKING_PREFIXES

    prefix = random.choice(BOOKING_PREFIXES)
    booking_ref = f"{prefix}{random.randint(100000, 999999)}"

    return (
        f"✅ Flight Booked Successfully!\n\n"
        f"Booking Reference: {booking_ref}\n"
        f"Flight: {flight_id}\n"
        f"Passenger: {passenger_name}\n"
        f"Confirmation sent to: {passenger_email}\n\n"
        f"Please check your email for boarding pass and details."
    )


@tool
def check_flight_availability(origin: str, destination: str, date_range: str) -> str:
    """
    Check flight availability for a date range.

    Args:
        origin: Departure city
        destination: Arrival city
        date_range: Date range (e.g., "June 1-7, 2024")

    Returns:
        Availability summary
    """
    # Get route info from demo data
    route_key = (origin, destination)
    reverse_route_key = (destination, origin)

    route_info = FLIGHT_ROUTES.get(route_key) or FLIGHT_ROUTES.get(reverse_route_key) or DEFAULT_ROUTE

    price_min, price_max = route_info["price_range"]
    avg_price = (price_min + price_max) // 2

    available_days = random.randint(4, 7)

    return (
        f"Flight Availability for {origin} → {destination}\n"
        f"Date Range: {date_range}\n\n"
        f"✓ {available_days} days with availability\n"
        f"Average Price: €{avg_price}\n"
        f"Best Deal: €{avg_price - 150} on weekday departures\n"
        f"Peak Price: €{avg_price + 200} on weekends"
    )
