from django.urls import path

from . import views

urlpatterns = [
    path('', views.getFood, name='food'),
    path('post/', views.postFood),
]
