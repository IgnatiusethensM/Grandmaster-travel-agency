from datetime import datetime, timedelta
import random

class FlightSearchService:
    def search(self, origin_code, destination_code, date):
        """
        Mock search for flights.
        Returns a list of dictionaries representing flights.
        """
        # Mock Airlines
        airlines = [
            {"code": "KQ", "name": "Kenya Airways", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Kenya_Airways_Logo.svg/1200px-Kenya_Airways_Logo.svg.png"},
            {"code": "ET", "name": "Ethiopian Airlines", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Ethiopian_Airlines_Logo.svg/1200px-Ethiopian_Airlines_Logo.svg.png"},
            {"code": "EK", "name": "Emirates", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Emirates_logo.svg/1200px-Emirates_logo.svg.png"},
            {"code": "QR", "name": "Qatar Airways", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Qatar_Airways_Logo.svg/1200px-Qatar_Airways_Logo.svg.png"},
        ]

        results = []
        base_price = 450
        
        # Generate 5 mock flights
        for i in range(5):
            airline = random.choice(airlines)
            departure_hour = random.randint(6, 22)
            duration_hours = random.randint(2, 12)
            
            # Create datetime objects (mocking)
            departure_time = datetime.strptime(f"{date} {departure_hour}:00", "%Y-%m-%d %H:%M")
            arrival_time = departure_time + timedelta(hours=duration_hours)
            
            flight = {
                "id": i + 1,
                "airline": airline,
                "flight_number": f"{airline['code']}{random.randint(100, 999)}",
                "origin": {"code": origin_code, "city": "Origin City"}, # Mock city names
                "destination": {"code": destination_code, "city": "Dest City"},
                "departure_time": departure_time,
                "arrival_time": arrival_time,
                "duration": f"{duration_hours}h 00m",
                "price": base_price + random.randint(-50, 200),
                "stops": 0 if duration_hours < 6 else 1
            }
            results.append(flight)
            
        return results
