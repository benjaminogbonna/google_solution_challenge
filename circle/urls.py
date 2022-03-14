from django.urls import path
from .import views

app_name = 'circle'

urlpatterns = [
    path('', views.ListCircle.as_view(), name='all'),
    path('create/', views.CreateCircle.as_view(), name='create'),
    path('members/in/<slug:slug>/', views.SingleCircle.as_view(), name='single'),
    path('join/<slug:slug>/', views.JoinCircle.as_view(), name='join'),
    path('leave/<slug:slug>/', views.LeaveCircle.as_view(), name='leave'),
]
