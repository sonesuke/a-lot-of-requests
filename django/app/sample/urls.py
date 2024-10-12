from django.urls import path

from . import views

urlpatterns = [
    path('sleep', views.sleep, name='sleep'),
    path('prime-number', views.prime_number, name='prime number'),
]