from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to = "profile_pictures")