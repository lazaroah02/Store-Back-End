from . models import UserProfile
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    name = serializers.CharField(max_length = 100, allow_blank=True)
    last_name = serializers.CharField(max_length = 200, allow_blank=True)
    phone = serializers.CharField(max_length=12, allow_blank=True)
    country = serializers.CharField(max_length=100, allow_blank=True)
    state = serializers.CharField(max_length=100, allow_blank=True)
    address = serializers.CharField(max_length=200, allow_blank=True)
    zip_code = serializers.CharField(max_length=10, allow_blank=True)
   
    class Meta:
        model = UserProfile
        fields = ['user', 'name', 'last_name', 'phone','country','state','address', 'zip_code']
        
    def update(self,instance, validated_data):
        return super().update(instance, validated_data)   
    
