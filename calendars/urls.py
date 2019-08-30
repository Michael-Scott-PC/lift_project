from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.calendars, name='calendars'),
    path('<abbr_month>/', views.calendar, name='calendar')
]