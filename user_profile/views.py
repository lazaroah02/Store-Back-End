from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import UserProfile
from .serializer import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserProfile_api(APIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    #get the user profile of the authenticated user
    def get(self, request): 
        try:
            profile = UserProfile.objects.get(user = request.user)
            return Response(
                {
                 "name": profile.name,
                 "last_name": profile.last_name,  
                 "phone":profile.phone,
                 'country':profile.country,
                 'state':profile.state,
                 "address":profile.address,
                 'zip_code':profile.zip_code,},
                status=status.HTTP_200_OK)
        except:
            return Response({"name": '',
                            "last_name": '',  
                            "phone":'',
                            'country':'',
                            'state':'',
                            "address":'',
                            'zip_code':''}, 
                        status=status.HTTP_404_NOT_FOUND)   
        
    
    #post to create a new user profile
    def post(self, request):
        try:
            serializer = self.serializer_class(data = {
                'user':request.user.id,
                'name':request.data['name'],
                'last_name' :request.data['last_name'],
                'phone' :request.data['phone'],
                'country' :request.data['country'],
                'state' :request.data['state'],
                'address' :request.data['address'],
                'zip_code' :request.data['zip_code'],
            })
            if serializer.is_valid() == False:
                return Response(status = status.HTTP_400_BAD_REQUEST)   
            serializer.save()
            return Response(status = status.HTTP_200_OK)
            
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)              
            
    #put to update the user profile
    def put(self, request):
        try:
            serializer = self.serializer_class(data = {
                    'user':request.user.id,
                    'name':request.data['name'],
                    'last_name' :request.data['last_name'],
                    'phone' :request.data['phone'],
                    'country' :request.data['country'],
                    'state' :request.data['state'],
                    'address' :request.data['address'],
                    'zip_code' :request.data['zip_code'],
                }
            )
            if serializer.is_valid() == False:
                return Response(status = status.HTTP_400_BAD_REQUEST)  
            
            profile = UserProfile.objects.get(user=request.user)
            if profile == None:
                return Response(status = status.HTTP_404_NOT_FOUND)
            serializer.update(profile, serializer.validated_data)
            return Response(status = status.HTTP_200_OK)
                
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)      
  