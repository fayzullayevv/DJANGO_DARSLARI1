from django.urls import path
from .views import About

urlpatterns = [
    path('about/',About)
]