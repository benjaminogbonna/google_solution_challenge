from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from circle.models import Circle, CircleMember

# Create your views here.


class CreateCircle(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Circle


class SingleCircle(generic.DetailView):
    model = Circle


