
import os
import django
from decimal import Decimal

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grandmaster_travel.settings')
django.setup()

from packages.models import Package, Destination, Category, PackageImage


def populate():
    print("Clearing existing packages...")
    Package.objects.all().delete()
    Destination.objects.all().delete()
    Category.objects.all().delete()
    PackageImage.objects.all().delete()

    print("Creating categories...")
    safari_cat = Category.objects.create(name="Safari", slug="safari")
    beach_cat = Category.objects.create(name="Beach", slug="beach")

    print("Creating destinations...")
    mombasa = Destination.objects.create(
        name="Mombasa",
        country="Kenya",
        slug="mombasa",
        description="A coastal city in southeastern Kenya along the Indian Ocean.",
        hero_image_url="https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1000&q=80"
    )
    mara = Destination.objects.create(
        name="Maasai Mara",
        country="Kenya",
        slug="maasai-mara",
        description="One of the most famous and important wildlife conservation and wilderness areas in Africa.",
        hero_image_url="https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80"
    )
    zanzibar = Destination.objects.create(
        name="Zanzibar",
        country="Tanzania",
        slug="zanzibar",
        description="An archipelago off the coast of East Africa, known for its beaches and Stone Town.",
        hero_image_url="https://images.unsplash.com/photo-1534764042898-10e30467b783?auto=format&fit=crop&w=1000&q=80"
    )

    print("Creating packages...")

    # Maasai Mara Package
    p1 = Package.objects.create(
        title="3 Days Maasai Mara Safari",
        slug="3-days-maasai-mara",
        destination=mara,
        category=safari_cat,
        price=Decimal("450.00"),
        duration_days=3,
        overview="Experience the thrill of the wild in the world-famous Maasai Mara. Witness the Big Five and the Great Migration (seasonal).",
        itinerary=[
            {"day": 1, "title": "Nairobi to Maasai Mara", "description": "Depart Nairobi and drive to Maasai Mara. Afternoon game drive."},
            {"day": 2, "title": "Full Day Game Drive", "description": "Spend the full day exploring the vast plains of the Mara tracking wildlife."},
            {"day": 3, "title": "Maasai Mara to Nairobi", "description": "Early morning game drive. Return to Nairobi in the afternoon."}
        ],
        inclusions=["Transport in safari van", "Full board accommodation", "Park entrance fees", "Game drives"],
        exclusions=["Tips", "Drinks", "Personal items"],
        is_featured=True
    )
    PackageImage.objects.create(package=p1, image_url="https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80", caption="Lions in Mara")

    # Mombasa Package
    p2 = Package.objects.create(
        title="5 Days Mombasa Beach Holiday",
        slug="5-days-mombasa-beach",
        destination=mombasa,
        category=beach_cat,
        price=Decimal("600.00"),
        duration_days=5,
        overview="Relax on the white sandy beaches of Mombasa. Enjoy water sports, cultural tours, and delicious seafood.",
        itinerary=[
            {"day": 1, "title": "Arrival in Mombasa", "description": "Arrive and transfer to your beach resort."},
            {"day": 2, "title": "Beach Relaxation", "description": "Full day at leisure on the beach."},
            {"day": 3, "title": "Mombasa City Tour", "description": "Visit Fort Jesus and Old Town."},
            {"day": 4, "title": "Marine Park Excursion", "description": "Snorkeling trip."},
            {"day": 5, "title": "Departure", "description": "Transfer to train station."}
        ],
        inclusions=["Accommodation", "Meals", "Transfers"],
        exclusions=["Flights", "Personal expenses"],
        is_featured=True
    )
    PackageImage.objects.create(package=p2, image_url="https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1000&q=80", caption="Mombasa Beach")

    # Zanzibar Package
    p3 = Package.objects.create(
        title="4 Days Zanzibar Getaway",
        slug="4-days-zanzibar",
        destination=zanzibar,
        category=beach_cat,
        price=Decimal("750.00"),
        duration_days=4,
        overview="Escape to the spice island of Zanzibar. Explore Stone Town and swim in crystal clear waters.",
        itinerary=[
            {"day": 1, "title": "Arrival in Zanzibar", "description": "Pick up and transfer to Stone Town hotel."},
            {"day": 2, "title": "Stone Town & Spice Tour", "description": "Guided walking tour."},
            {"day": 3, "title": "Beach Transfer", "description": "Transfer to Nungwi beach."},
            {"day": 4, "title": "Departure", "description": "Transfer to airport."}
        ],
        inclusions=["Hotel stays", "Tours", "Transfers"],
        exclusions=["International flights", "Visa fees"],
        is_featured=True
    )
    PackageImage.objects.create(package=p3, image_url="https://images.unsplash.com/photo-1534764042898-10e30467b783?auto=format&fit=crop&w=1000&q=80", caption="Stone Town")

    print("Database populated successfully!")


if __name__ == '__main__':
    populate()
