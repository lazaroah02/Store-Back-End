from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import UserProfile

# Create your views here.
class UserProfile_api(APIView):
    def get(self, request): 
        profile = UserProfile.objects.get(user = request.user)
        return Response({"phone":profile.phone,"address":profile.address,"description":profile.description,"photo":profile.photo.url},status=status.HTTP_200_OK)