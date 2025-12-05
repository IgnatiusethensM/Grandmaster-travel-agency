# Grandmaster Travel Agency

A comprehensive travel booking platform built with Django, featuring flight, hotel, transfer, and safari booking capabilities.

## Features

- **Flight Booking**: Search and book flights (Mock integration).
- **Hotel Booking**: Search local and partner hotels (Mock Booking.com integration).
- **Transfers**: Book airport transfers and local rides with price estimation.
- **Safari Packages**: Explore and book exclusive safari tours.
- **User Dashboard**: Manage bookings and view trip details.
- **Responsive Design**: Modern, mobile-friendly UI with glassmorphism effects.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd grandmaster-travel-agency
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Project Structure

- `grandmaster_travel/`: Main project settings and URLs.
- `web/`: Home page and static content.
- `flights/`: Flight booking logic.
- `hotels/`: Hotel booking logic and mock service.
- `transfers/`: Transfer booking logic.
- `packages/`: Safari and tour packages.
- `bookings/`: Centralized booking management.
- `core/`: User authentication and core utilities.

## Technologies

- **Backend**: Django 5.2
- **Frontend**: HTML5, CSS3 (Custom), JavaScript
- **Database**: SQLite (Dev), PostgreSQL (Prod ready)
- **Styling**: Custom CSS with Glassmorphism design system.
