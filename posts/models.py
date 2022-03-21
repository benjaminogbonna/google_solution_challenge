from django.db import models
from django.urls import reverse
from circle.models import Circle
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.CharField(verbose_name="Message", max_length=50, default='')
    start = models.CharField(verbose_name="Start", max_length=100, default='')
    destination = models.CharField(verbose_name="Destination", max_length=100, default='')
    circle = models.ForeignKey(Circle, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message = self.message
        self.start = self.start
        self.destination = self.destination
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username,
                                               'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message', 'start', 'destination']
