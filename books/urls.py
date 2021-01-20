from django.urls import path, include
from . import views

urlpatterns = [
        path('viewbook/', views.viewbook, name='viewbook'),
    ]