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
            "image": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=800&q=80"
        },
        {
            "id": 2,
            "name": "Masai Mara Wildlife Tour",
            "destination": "Kenya",
            "price": 3800,
            "duration": "5 Days",
            "image": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=800&q=80"
        },
        {
            "id": 3,
            "name": "Cape Town & Safari Combo",
            "destination": "South Africa",
            "price": 5200,
            "duration": "10 Days",
            "image": "https://images.unsplash.com/photo-1576485290814-1c72aa4bbb8e?auto=format&fit=crop&w=800&q=80"
        },
        {
            "id": 4,
            "name": "Victoria Falls Adventure",
            "destination": "Zimbabwe",
            "price": 2800,
            "duration": "4 Days",
            "image": "https://images.unsplash.com/photo-1489392191049-fc10c97e64b6?auto=format&fit=crop&w=800&q=80"
        }
    ]

    destinations = [
        {"id": 1, "name": "Safari", "description": "Witness the Big Five", "image": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=600&q=80"},
        {"id": 2, "name": "Beach", "description": "Pristine coastal escapes", "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80"},
        {"id": 3, "name": "Mountain", "description": "Conquer majestic peaks", "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=600&q=80"},
        {"id": 4, "name": "Cultural", "description": "Immersive local experiences", "image": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?auto=format&fit=crop&w=600&q=80"},
        {"id": 5, "name": "Desert", "description": "Explore vast landscapes", "image": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=600&q=80"}
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
            "image": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=150&q=80"
        },
        {
            "id": 2,
            "name": "James Cooper",
            "location": "New York, USA",
            "rating": 5,
            "text": "The gorilla trekking experience in Rwanda was life-changing. Absolutely worth it!",
            "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"
        },
        {
            "id": 3,
            "name": "Emma Thompson",
            "location": "Sydney, Australia",
            "rating": 5,
            "text": "From the Victoria Falls to the Okavango Delta, every moment was magical.",
            "image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=150&q=80"
        }
    ]

    articles = [
        {
            "id": 1,
            "title": "Best Time to Visit the Serengeti",
            "excerpt": "Discover the optimal seasons for witnessing the Great Migration.",
            "date": "November 15, 2025",
            "image": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=600&q=80",
            "category": "Travel Tips"
        },
        {
            "id": 2,
            "title": "Gorilla Trekking: A Complete Guide",
            "excerpt": "Everything you need to know about preparing for an unforgettable trek.",
            "date": "November 10, 2025",
            "image": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=600&q=80",
            "category": "Adventure"
        },
        {
            "id": 3,
            "title": "Victoria Falls: Natural Wonder",
            "excerpt": "Explore the majesty of Victoria Falls and the surrounding attractions.",
            "date": "November 5, 2025",
            "image": "https://images.unsplash.com/photo-1489392191049-fc10c97e64b6?auto=format&fit=crop&w=600&q=80",
            "category": "Destinations"
        }
    ]

    footer_destinations = [
        "Kenya Safaris", "Tanzania Tours", "South Africa",
        "Rwanda Gorillas", "Botswana", "Namibia"
    ]

    nav_links = [
        {"name": "Destinations", "href": "#destinations"},
        {"name": "Tours", "href": "#tours"},
        {"name": "About", "href": "#about"},
        {"name": "Contact", "href": "#contact"}
    ]

    context = {
        "tours": tours,
        "destinations": destinations,
        "features": features,
        "testimonials": testimonials,
        "articles": articles,
        "footer_destinations": footer_destinations,
        "nav_links": nav_links,
        "destinations_options": [
            {"value": "kenya", "label": "Kenya"},
            {"value": "tanzania", "label": "Tanzania"},
            {"value": "south_africa", "label": "South Africa"},
            {"value": "rwanda", "label": "Rwanda"},
            {"value": "uganda", "label": "Uganda"},
        ],
        "year": datetime.now().year
    }

    return render(request, 'home.html', context)
