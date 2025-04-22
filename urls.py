from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('cal', views.calendar, name="calendar"),
]
