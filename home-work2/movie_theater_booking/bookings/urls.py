from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, seat_booking, booking_history

router = DefaultRouter()
router.register(r'api/movies', MovieViewSet, basename='movie')
router.register(r'api/movies', MovieViewSet, basename='movies')
router.register(r'api/seats', SeatViewSet, basename='seats')
router.register(r'api/bookings', BookingViewSet, basename='bookings')

urlpatterns = [
    path('', include(router.urls)),
    path('', movie_list, name='movie_list'),
    path('movies/', movie_list, name='movie_list'),  # Movie listing page
    path('book/<int:movie_id>/', seat_booking, name='seat_booking'),
    path('history/', booking_history, name='booking_history'),  # Booking history page
]
