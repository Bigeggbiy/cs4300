from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('bookings.urls', 'bookings'), namespace='api')),    path('', include('bookings.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]
