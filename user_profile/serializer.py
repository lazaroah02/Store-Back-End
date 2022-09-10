from . models import UserProfile
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    phone = serializers.CharField(max_length=12, allow_blank=True)
    address = serializers.CharField(max_length=200, allow_blank=True)
    photo = serializers.ImageField(allow_empty_file = True)
    description = serializers.CharField(allow_blank=True, style={'input_type': 'text'})
    
    class Meta:
        model = UserProfile
        fields = ['user','phone','address','photo','description']
        
    def update(self,instance, validated_data):
        return super().update(instance, validated_data)   
    
