Movie Theater Booking Application
---------------------------------

Project Overview:
-----------------
Movie Theater Booking is a Django-based web application that allows users to view available movies,
book seats in a theater, and view their booking history. The project also provides a RESTful API
using Django REST Framework for managing movies, seats, and bookings.

Project Structure:
------------------
movie_theater_booking/
│
├── bookings/
│   ├── migrations/              # Database migrations
│   ├── templates/
│   │   └── bookings/            # HTML templates for the application
│   │       ├── base.html        # Base template with Bootstrap for responsive design
│   │       ├── movie_list.html  # Template for listing movies
│   │       ├── seat_booking.html# Template for booking seats
│   │       └── booking_history.html  # Template for displaying booking history
│   ├── __init__.py
│   ├── admin.py                 # Admin panel configuration
│   ├── apps.py
│   ├── models.py                # Models for Movie, Seat, and Booking
│   ├── serializers.py           # Serializers for REST API endpoints
│   ├── tests.py                 # Unit tests and integration tests
│   ├── urls.py                 # URL routing for the bookings app
│   └── views.py                 # Views and API viewsets
│
├── movie_theater_booking/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # Project settings, including installed apps and ALLOWED_HOSTS
│   ├── urls.py                 # Root URL configuration
│   └── wsgi.py
│
├── manage.py                    # Django management script
└── readme.txt                   # This file


Running the Application:
------------------------
1. Start the development server on port 3000
   > python manage.py runserver 0.0.0.0:3000

2. Access the application in your web browser:
   - Main site: http://127.0.0.1:3000/movies (Movie listings, seat booking)
   - Admin panel: http://127.0.0.1:3000/admin/
   - API endpoints:
     * Movies API: http://127.0.0.1:3000/api/movies/
     * Seats API: http://127.0.0.1:3000/api/seats/
     * Bookings API: http://127.0.0.1:3000/api/bookings/

Testing:
--------
1. Run unit tests and integration tests:
   > python manage.py test bookings

Deployment on DevEdu:
---------------------
1. check your ALLOWED_HOSTS setting in settings.py
2. Run the server on port 3000:
   > python manage.py runserver 0.0.0.0:3000
3. In DevEdu, click the "App" button to view your current application.