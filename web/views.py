from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.http import Http404
from packages.models import Package, Destination

def home(request):
    # Fetch featured packages dynamically
    safari_packages = Package.objects.filter(is_featured=True)[:3]
    if not safari_packages:
        safari_packages = Package.objects.all()[:3]
    
    # Fetch destinations dynamically
    destinations = Destination.objects.all()[:6]

    context = {
        "nav_links": [
            {"name": "Home", "href": "/"},
            {
                "name": "Blog",
                "href": "#blog",
                "dropdown": [
                    {"name": "Travel Tips", "href": "#"},
                    {"name": "Wildlife Guide", "href": "#"},
                    {"name": "Cultural Insights", "href": "#"}
                ]
            }
        ],
        "year": datetime.now().year,
        "featured_services": [
            {"name": "Hotels", "icon": "bed", "desc": "Luxury stays at affordable rates"},
            {"name": "Trains", "icon": "train", "desc": "Scenic rail journeys across Africa"},
            {"name": "Taxis", "icon": "car", "desc": "Reliable airport transfers & local rides"},
            {"name": "Safaris", "icon": "compass", "desc": "Unforgettable wildlife experiences"}
        ],
        "destinations": destinations,
        "testimonials": [
            {
                "name": "Sarah Mitchell",
                "location": "London, UK",
                "rating": 5,
                "text": "Our Maasai Mara safari exceeded all expectations. The guides were incredibly knowledgeable.",
                "image": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=150&q=80",
                "service": "Safari Package"
            },
            {
                "name": "James Cooper",
                "location": "New York, USA",
                "rating": 5,
                "text": "The beach holiday in Zanzibar was life-changing. Absolutely worth it!",
                "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80",
                "service": "Adventure Tour"
            },
            {
                "name": "Emma Thompson",
                "location": "Sydney, Australia",
                "rating": 5,
                "text": "From Mombasa to the tsavo, every moment was magical.",
                "image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=150&q=80",
                "service": "Custom Itinerary"
            }
        ],
        "safari_packages": safari_packages,
        "special_offers": [
            {
                "title": "Christmas in Mombasa",
                "discount": "20% OFF",
                "price": 1200,
                "original_price": 1500,
                "image": "https://images.unsplash.com/photo-1576485290814-1c72aa4bbb8e?auto=format&fit=crop&w=800&q=80",
                "expiry": "2 Days Left"
            },
            {
                "title": "Zanzibar Beach Escape",
                "discount": "15% OFF",
                "price": 950,
                "original_price": 1100,
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
                "expiry": "5 Days Left"
            }
        ]
    }
    return render(request, 'home.html', context)

def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    
    context = {
        "destination": destination,
        "year": datetime.now().year,
        "nav_links": [
            {"name": "Home", "href": "/"},
            {
                "name": "Blog",
                "href": "#blog",
                "dropdown": [
                    {"name": "Travel Tips", "href": "#"},
                    {"name": "Wildlife Guide", "href": "#"},
                    {"name": "Cultural Insights", "href": "#"}
                ]
            }
        ]
    }
    return render(request, 'web/destination_detail.html', context)

def safari_package_detail(request, slug):
    package = get_object_or_404(Package, slug=slug)
    
    context = {
        "package": package,
        "year": datetime.now().year,
        "nav_links": [
            {"name": "Home", "href": "/"},
            {
                "name": "Blog",
                "href": "#blog",
                "dropdown": [
                    {"name": "Travel Tips", "href": "#"},
                    {"name": "Wildlife Guide", "href": "#"},
                    {"name": "Cultural Insights", "href": "#"}
                ]
            }
        ]
    }
    return render(request, 'web/safari_detail.html', context)

def safari_packages(request):
    # Fetch all safari packages
    packages = Package.objects.all()
    destinations = Destination.objects.all()

    # Create distinct features list (mock or static for now)
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
            "text": "Our Maasai Mara safari exceeded all expectations. The guides were incredibly knowledgeable.",
            "image": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=150&q=80"
        },
        {
            "id": 2,
            "name": "James Cooper",
            "location": "New York, USA",
            "rating": 5,
            "text": "The beach holiday in Zanzibar was life-changing. Absolutely worth it!",
            "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80"
        },
        {
            "id": 3,
            "name": "Emma Thompson",
            "location": "Sydney, Australia",
            "rating": 5,
            "text": "From Mombasa to the tsavo, every moment was magical.",
            "image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=150&q=80"
        }
    ]

    articles = [
        {
            "id": 1,
            "title": "Best Time to Visit Maasai Mara",
            "excerpt": "Discover the optimal seasons for witnessing the Great Migration.",
            "date": "November 15, 2025",
            "image": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=600&q=80",
            "category": "Travel Tips"
        },
        {
            "id": 2,
            "title": "Zanzibar Beaches: A Complete Guide",
            "excerpt": "Everything you need to know about where to stay on the island.",
            "date": "November 10, 2025",
            "image": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=600&q=80",
            "category": "Beach"
        },
        {
            "id": 3,
            "title": "Mombasa Old Town: History & Culture",
            "excerpt": "Explore the majesty of Fort Jesus and the surrounding attractions.",
            "date": "November 5, 2025",
            "image": "https://images.unsplash.com/photo-1489392191049-fc10c97e64b6?auto=format&fit=crop&w=600&q=80",
            "category": "Destinations"
        }
    ]

    context = {
        "tours": packages, # The template expects 'tours'
        "destinations": destinations,
        "features": features,
        "testimonials": testimonials,
        "articles": articles,
        "footer_destinations": ["Mombasa", "Maasai Mara", "Zanzibar"],
        "nav_links": [
            {"name": "Home", "href": "/"},
            {
                "name": "Blog",
                "href": "#blog",
                "dropdown": [
                    {"name": "Travel Tips", "href": "#"},
                    {"name": "Wildlife Guide", "href": "#"},
                    {"name": "Cultural Insights", "href": "#"}
                ]
            }
        ],
        "destinations_options": [
            {"value": "kenya", "label": "Kenya"},
            {"value": "tanzania", "label": "Tanzania"},
        ],
        "year": datetime.now().year
    }
    return render(request, 'web/safari_packages.html', context)
