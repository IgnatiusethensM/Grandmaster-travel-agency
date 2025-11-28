from django.shortcuts import render
from datetime import datetime

def home(request):
    # Data Models (Hardcoded for Design Match)
    tours = [
        {
            "id": 1,
            "name": "Serengeti Safari Experience",
            "destination": "Tanzania",
            "price": 4500,
            "duration": "7 Days",
            "image": "https://images.unsplash.com/photo-1728891386152-8cf2f86ad"
        },
        {
            "id": 2,
            "name": "Masai Mara Wildlife Tour",
            "destination": "Kenya",
            "price": 3800,
            "duration": "5 Days",
            "image": "https://images.unsplash.com/photo-1611519183412-4db57afd1"
        },
        {
            "id": 3,
            "name": "Cape Town & Safari Combo",
            "destination": "South Africa",
            "price": 5200,
            "duration": "10 Days",
            "image": "https://images.unsplash.com/photo-1732189860851-232d8bd82"
        },
        {
            "id": 4,
            "name": "Victoria Falls Adventure",
            "destination": "Zimbabwe",
            "price": 2800,
            "duration": "4 Days",
            "image": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5"
        }
    ]

    destinations = [
        {"id": 1, "name": "Safari", "description": "Witness the Big Five", "image": "https://images.unsplash.com/photo-1686420724802-87fa967a2"},
        {"id": 2, "name": "Beach", "description": "Pristine coastal escapes", "image": "https://images.unsplash.com/photo-1699955376108-9274ed93d"},
        {"id": 3, "name": "Mountain", "description": "Conquer majestic peaks", "image": "https://images.unsplash.com/photo-1489392191049-fc10c97e6"},
        {"id": 4, "name": "Cultural", "description": "Immersive local experiences", "image": "https://images.unsplash.com/photo-1746189897983-ffd3a582a"},
        {"id": 5, "name": "Desert", "description": "Explore vast landscapes", "image": "https://images.unsplash.com/photo-1509316785289-025f5b8"}
    ]

    features = [
        {"id": 1, "icon": "award", "title": "Expert Guides", "description": "Experienced local guides with deep knowledge of African wildlife and culture."},
        {"id": 2, "icon": "users", "title": "Small Groups", "description": "Intimate group sizes for personalized attention and authentic experiences."},
        {"id": 3, "icon": "globe", "title": "Sustainable Travel", "description": "Committed to responsible tourism that benefits local communities."},
        {"id": 4, "icon": "shield", "title": "Safety First", "description": "Comprehensive safety measures and 24/7 support throughout your journey."}
    ]

    testimonials = [
        {
            "id": 1,
            "name": "Sarah Mitchell",
            "location": "London, UK",
            "rating": 5,
            "text": "Our Serengeti safari exceeded all expectations. The guides were incredibly knowledgeable.",
            "image": "https://images.unsplash.com/photo-1764090317825-9b76e437"
        },
        {
            "id": 2,
            "name": "James Cooper",
            "location": "New York, USA",
            "rating": 5,
            "text": "The gorilla trekking experience in Rwanda was life-changing. Absolutely worth it!",
            "image": "https://images.unsplash.com/photo-1764090317825-9b76e437"
        },
        {
            "id": 3,
            "name": "Emma Thompson",
            "location": "Sydney, Australia",
            "rating": 5,
            "text": "From the Victoria Falls to the Okavango Delta, every moment was magical.",
            "image": "https://images.unsplash.com/photo-1764090317825-9b76e437"
        }
    ]

    articles = [
        {
            "id": 1,
            "title": "Best Time to Visit the Serengeti",
            "excerpt": "Discover the optimal seasons for witnessing the Great Migration.",
            "date": "November 15, 2025",
            "image": "https://images.unsplash.com/photo-1728891386152-8cf2f86ad",
            "category": "Travel Tips"
        },
        {
            "id": 2,
            "title": "Gorilla Trekking: A Complete Guide",
            "excerpt": "Everything you need to know about preparing for an unforgettable trek.",
            "date": "November 10, 2025",
            "image": "https://images.unsplash.com/photo-1670191996981-22246a4eb",
            "category": "Adventure"
        },
        {
            "id": 3,
            "title": "Victoria Falls: Natural Wonder",
            "excerpt": "Explore the majesty of Victoria Falls and the surrounding attractions.",
            "date": "November 5, 2025",
            "image": "https://images.unsplash.com/photo-1670259317136-ef2f1007a",
            "category": "Destinations"
        }
    ]

    footer_destinations = [
        "Kenya Safaris", "Tanzania Tours", "South Africa",
        "Rwanda Gorillas", "Botswana", "Namibia"
    ]

    context = {
        "tours": tours,
        "destinations": destinations,
        "features": features,
        "testimonials": testimonials,
        "articles": articles,
        "footer_destinations": footer_destinations,
        "year": datetime.now().year
    }

    return render(request, 'home.html', context)
