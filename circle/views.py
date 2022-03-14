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
    model = Circle
    fields = ('name', 'description')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # CircleMember.objects.create(member=self.request.user, circle=self.object)
        # CircleMember.member(member=self.request.user, circle=self.object)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class SingleCircle(generic.DetailView):
    model = Circle


class ListCircle(generic.ListView):
    model = Circle


class JoinCircle(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('circle:single', kwargs={'slug': kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        circle = get_object_or_404(Circle, slug=self.kwargs.get('slug'))
        try:
            CircleMember.objects.create(member=self.request.user, circle=circle)
        except IntegrityError:
            messages.warning(self.request, 'Already a member!')
        else:
            messages.success(self.request, 'You are now a member')

        return super().get(request, *args, **kwargs)


class LeaveCircle(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('circle:all')

    def get(self, request, *args, **kwargs):
        try:
            membership = CircleMember.objects.filter(
                member=self.request.user,
                circle__slug=self.kwargs.get('slug')
            ).get()
        except CircleMember.DoesNotExist:
            messages.warning(self.request, 'Sorry, you are not int this circle!')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the circle!')

        return super().get(request, *args, **kwargs)
