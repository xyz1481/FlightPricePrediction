from django.contrib import admin
from django.urls import path
from core.views import predict_flight_price

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', predict_flight_price, name='predict'),
]