from django.urls import path
from .views import Contact 

urlpatterns = [
    path('contact/',Contact)
]
