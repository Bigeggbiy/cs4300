from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets, permissions
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import action


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]  # Public access


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=["post"])
    def book(self, request, pk=None):
        seat = get_object_or_404(Seat, pk=pk)
        if seat.is_booked:
            return Response({"error": "Seat already booked"}, status=400)

        booking = Booking.objects.create(user=request.user, seat=seat, movie=seat.movie)
        seat.is_booked = True
        seat.save()

        return Response(BookingSerializer(booking).data)


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "bookings/movie_list.html", {"movies": movies})


@login_required
def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all()

    if request.method == "POST":
        seat_id = request.POST.get("seat_id")
        seat = get_object_or_404(Seat, id=seat_id)

        if not seat.is_booked:
            Booking.objects.create(movie=movie, seat=seat, user=request.user)
            seat.is_booked = True
            seat.save()
            return redirect("booking_history")

    return render(
        request, "bookings/seat_booking.html", {"movie": movie, "seats": seats}
    )


@login_required  # Ensures only logged-in users can access
def booking_history(request):
    user = request.user

    if not user.is_authenticated:
        return redirect("login")  # Redirect to login page if not authenticated

    user_bookings = Booking.objects.filter(user=user)
    return render(request, "bookings/booking_history.html", {"bookings": user_bookings})
