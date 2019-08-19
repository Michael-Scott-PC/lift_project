from django.shortcuts import render

# Create your views here.
def calendars(request):
    return render(request, 'calendars/calendars.html')

def calendar(request):
    return render(request, 'calendars/calendar.html')