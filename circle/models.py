from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Circle(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    members = models.ManyToManyField(User, through='CircleMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = self.description
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('circle:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class CircleMember(models.Model):
    circle = models.ForeignKey(Circle, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='circle_members', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('circle', 'user')
