import calendar
from datetime import datetime
from datetime import date
from calendar import Calendar
from .models import Event

class FullCalendar(calendar.TextCalendar):
    """Create a full 12 month calendar for the current year"""

    this_year = date.today().year

    def __init__(self, firstweekday=6):
        """ Make Sunday the first day of the week for every instance """
        self.firstweekday = firstweekday
        return

    def generate_month_lst(self):
        """ Create a list of strings containing the full month names """
        full_month_names = calendar.month_name
        month_lst = []
        for month in full_month_names:
            month_lst.append(month)
        del month_lst[0]
        return month_lst

    def generate_abbr_month_lst(self):
        """ Create a list of strings containing the abbr month names """
        abbr_month_names = calendar.month_abbr
        abbr_month_lst = []
        for abbr_month in abbr_month_names:
            abbr_month_lst.append(abbr_month)
        del abbr_month_lst[0]
        return abbr_month_lst

    def generate_abbr_weekday_lst(self):
        """ Create a list of weekday name abbreviations containing 2 letters """
        abbr_weekday_names = calendar.day_abbr
        abbr_weekday_lst = []
        for abbr in abbr_weekday_names:
            abbr = abbr.replace(abbr[-1], '')
            abbr_weekday_lst.append(abbr)
        return abbr_weekday_lst

    def generate_monthdays_lst(self):
        """ Create a list of sublists containing monthday integers for each month """
        this_year = date.today().year
        cal = calendar.Calendar(firstweekday=6)
        flat_lst = []
        for month in range(1, 13):
            days = cal.monthdayscalendar(this_year, month)
            f_lst = [num for sublist in days for num in sublist]
            flat_lst.append(f_lst)
        return flat_lst

    def create_month_days_dict(self, month_lst, flat_lst):
        """ Merge the month and days lists into a dictionary. key = month, value = list of days(ints)"""
        month_days_dict = {}
        x = 1
        y = 0
        while x < 13:
            for month in month_lst:
                if month not in month_days_dict:
                    for days_lst in flat_lst[y:x]:
                        month_days_dict[month] = days_lst
                        x = x + 1
                        y = y + 1
        return month_days_dict
