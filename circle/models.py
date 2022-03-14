from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django import template

from django.contrib.auth import get_user_model

# register = template.Library()
User = get_user_model()

# Create your models here.


class Circle(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="circle_owner", null=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    members = models.ManyToManyField(User, through='CircleMember')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description = self.description
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('circle:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name', 'owner']


class CircleMember(models.Model):
    circle = models.ForeignKey(Circle, related_name='memberships', on_delete=models.CASCADE)
    member = models.ForeignKey(User, related_name='circle_members', on_delete=models.CASCADE)

    def __str__(self):
        return self.member.username

    class Meta:
        unique_together = ('circle', 'member')
