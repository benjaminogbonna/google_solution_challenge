from django.db import models
from django.conf import settings
from circle.models import Circle, CircleMember


# Create your models here.
USER_TYPE = (
    ('vip', 'VIP'),
    ('helper', 'Helper'),
)

GENDER = (
    ('female', 'Female'),
    ('male', 'Male'),
)


# A class to extend registration
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_type = models.CharField(verbose_name='User type', max_length=10, choices=USER_TYPE, null=True, blank=True)
    gender = models.CharField(verbose_name="Gender", max_length=10, choices=GENDER, null=True, blank=True)
    phone = models.CharField(verbose_name="Phone", max_length=20, null=True, blank=True)
    address = models.CharField(verbose_name="Address", max_length=100, null=True, blank=True)
    town = models.CharField(verbose_name="Town/City", max_length=100, null=True, blank=True)
    # post_code = models.CharField(verbose_name="Post Code", max_length=8, null=True, blank=True)
    country = models.CharField(verbose_name="Country", max_length=100, null=True, blank=True)
    # longitude = models.CharField(verbose_name="Longitude", max_length=50, null=True, blank=True)
    # latitude = models.CharField(verbose_name="Latitude", max_length=50, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    # circles = models.ManyToManyField(Circle, through=CircleMember, related_name='circle_member')

    def __str__(self):
        return f'Profile for user {self.user.username}'
