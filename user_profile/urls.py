from django.urls import path
from .views import UserProfile_api

urlpatterns = [
    path('', UserProfile_api.as_view()),
]
