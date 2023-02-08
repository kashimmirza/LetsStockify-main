
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.stockPickers, name='stockpicker'),
    path('stocktracker/', views.stockTracker, name='stocktracker'),
]
