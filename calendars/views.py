from django.shortcuts import render
from .months_days import months, days, january, february, march, april, may, june, july, august, september, october, november, december
from django.http import HttpResponse

# Create your views here.
def calendars(request):

    context = {
        'months': months,
        'days': days,
        'january': january,
        'february': february,
        'march': march,
        'april': april,
        'may': may,
        'june': june,
        'july': july,
        'august': august,
        'september': september,
        'october': october,
        'november': november,
        'december': december
    }

    return render(request, 'calendars/calendars.html', context)

def calendar(request):
    context = {
        'months': months,
        'days': days,
        'january': january,
        'february': february,
        'march': march,
        'april': april,
        'may': may,
        'june': june,
        'july': july,
        'august': august,
        'september': september,
        'october': october,
        'november': november,
        'december': december
    }
    
    return render(request, 'calendars/calendar.html', context)