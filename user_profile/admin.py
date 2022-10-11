from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'last_name', 'phone','country','state','address', 'zip_code')
admin.site.register(UserProfile, UserProfileAdmin)