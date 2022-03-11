from django.urls import path
from .import views

app_name = 'circle'

urlpatterns = [
    path('create/', views.CreateCircle.as_view(), name='create'),
    path('members/in/<slug:slug>/', views.SingleCircle.as_view(), name='single'),

]
