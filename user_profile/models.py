from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length = 10, blank=True, null=True)
