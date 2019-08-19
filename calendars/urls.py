from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.calendars, name='calendars'),
    path('<int:calendar_id>', views.calendar, name='calendar')
]