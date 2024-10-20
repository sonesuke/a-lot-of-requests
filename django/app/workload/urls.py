from django.urls import path

from . import views

urlpatterns = [
    path('no-load', views.sleep, name='no load'),
    path('sleep', views.sleep, name='sleep'),
    path('async-sleep', views.async_sleep, name='async-sleep'),
    path('prime-number', views.prime_number, name='prime number'),
    path('celery-prime-number', views.celery_prime_number_view, name='celery prime number'),
]