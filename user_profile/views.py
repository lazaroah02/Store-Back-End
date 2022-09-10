from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import UserProfile
from .serializer import UserProfileSerializer

# Create your views here.
class UserProfile_api(APIView):
    serializer_class = UserProfileSerializer
    
    #get the user profile of the authenticated user
    def get(self, request): 
        try:
            profile = UserProfile.objects.get(user = request.user)
            return Response(
                {"phone":profile.phone,"address":profile.address,"description":profile.description,"photo":profile.photo.url},
                status=status.HTTP_200_OK)
        except:
            return Response({"message":"No tienes perfil creado"})
        
    
    #post to create a new user profile
    def post(self, request):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid() and serializer.validated_data["user"] == request.user:
                serializer.save()
                return Response(status = status.HTTP_200_OK)
            else:
                return Response(status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)    
        
    #put to update the user profile
    def put(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid() and serializer.validated_data["user"] == request.user:
            profile = UserProfile.objects.get(user=request.user)
            if profile != None:
                serializer.update(profile, serializer.validated_data)
                return Response(status = status.HTTP_200_OK)
            else:
                return Response(status = status.HTTP_404_NOT_FOUND)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)    