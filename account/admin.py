from django.contrib import admin
from . models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type', 'gender', 'country']
    search_fields = ['user', 'country', 'town']
    list_filter = ['gender', 'country', 'user_type']
