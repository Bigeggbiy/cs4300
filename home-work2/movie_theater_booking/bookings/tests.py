from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from .models import Movie, Seat, Booking


# Unit tests for models
class MovieModelTest(TestCase):
    def test_create_movie(self):
        movie = Movie.objects.create(
            title="Test Movie",
            description="A sample movie for testing.",
            release_date="2025-01-01",
            duration=120,
        )
        self.assertEqual(movie.title, "Test Movie")
        self.assertEqual(Movie.objects.count(), 1)


class SeatModelTest(TestCase):
    def test_create_seat(self):
        seat = Seat.objects.create(seat_number="A1", is_booked=False)
        self.assertEqual(seat.seat_number, "A1")
        self.assertFalse(seat.is_booked)


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A sample movie for testing.",
            release_date="2025-01-01",
            duration=120,
        )
        self.seat = Seat.objects.create(seat_number="A1", is_booked=False)

    def test_create_booking(self):
        booking = Booking.objects.create(
            movie=self.movie, seat=self.seat, user=self.user
        )
        self.assertEqual(booking.movie, self.movie)
        self.assertEqual(booking.seat, self.seat)
        self.assertEqual(booking.user, self.user)


# Integration tests for API endpoints using Django REST Framework
class APITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="apitestuser", password="12345")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.movie = Movie.objects.create(
            title="API Test Movie",
            description="A sample movie for API testing.",
            release_date="2025-01-01",
            duration=120,
        )
        self.seat = Seat.objects.create(seat_number="B1", is_booked=False)

    def test_get_movies_api(self):
        # Use the namespaced URL for the movies list endpoint.
        url = reverse("api:movies-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Now response.data should be available.
        self.assertIsInstance(response.data, list)

    def test_get_seats_api(self):
        url = reverse("seats-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

    def test_create_booking_api(self):
        # Attempt to create a new booking via the API.
        # Note: Your BookingSerializer may be configured as read-only for nested fields.
        # If so, you might need to modify it to accept movie and seat IDs for creation.
        url = reverse("bookings-list")
        data = {"movie": self.movie.id, "seat": self.seat.id}
        response = self.client.post(url, data, format="json")
        # Expect HTTP 201 CREATED if the booking is successfully created.
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 1)
