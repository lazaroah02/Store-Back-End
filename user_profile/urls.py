from django.urls import path
from . import views 

urlpatterns = [
    path('', views.UserProfile_api.as_view()),
]
