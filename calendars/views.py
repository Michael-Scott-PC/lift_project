from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .months_days import FullCalendar
from .models import Event
from exercises.models import Exercise


def calendars(request):
    #events = Event.objects.all()

    cal = FullCalendar()
    current_year = cal.this_year
    months = cal.generate_month_lst()
    abbr_months = cal.generate_abbr_month_lst()
    abbr_weekdays = cal.generate_abbr_weekday_lst()
    month_days = cal.generate_monthdays_lst()
    month_days_dict = cal.create_month_days_dict(months, month_days)

    context = {
        'current_year': current_year,
        'months': months,
        'abbr_months': abbr_months,
        'monday_days': month_days,
        'abbr_weekdays': abbr_weekdays,
        'month_days_dict': month_days_dict,
        #'events': events
        }

    return render(request, 'calendars/calendars.html', context)

def calendar(request, abbr_month):
    events = Event.objects.all()
    
    cal = FullCalendar()
    current_year = cal.this_year
    months = cal.generate_month_lst()
    abbr_months = cal.generate_abbr_month_lst()
    abbr_month_nums_dict = cal.abbr_month_numbers_dict()
    abbr_weekdays = cal.generate_abbr_weekday_lst()
    month_days = cal.generate_monthdays_lst()
    month_days_dict = cal.create_month_days_dict(months, month_days)

    context = {
        'abbr_month': abbr_month,
        'current_year': current_year,
        'months': months,
        'abbr_months': abbr_months,
        'abbr_month_nums_dict': abbr_month_nums_dict,
        'monday_days': month_days,
        'abbr_weekdays': abbr_weekdays,
        'month_days_dict': month_days_dict,
        'events': events,
    }

    return render(request, 'calendars/calendar.html', context)