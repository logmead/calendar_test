from django.shortcuts import render
from .forms import CalendarForm
from .utils import *

def main(request):
    template = "calendar_test/main.html"
    return render(request, template)

def calendar(request):
    template = "calendar_test/calendar.html"

    current_date = TODAY()

    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            current_date = form.cleaned_data['date_field']
    # first day of the month
    first_day = dt.date(year=current_date.year, month=current_date.month, day=1)
    # what day does the first week actually start from 
    render_first_day = first_day - dt.timedelta(days=first_day.weekday())
    
    year = current_date.year
    month = current_date.month
    first_week_day = render_first_day

    # about to populate actual days to render
    weeks = []

    while 1:
        last_week_day = first_week_day + dt.timedelta(days=7)
        # get the whole week of days and append them
        week = []
        for i in range(0, 7):
            dat = first_week_day + dt.timedelta(days=i)
            week.append({
                'day' : dat,
                'string' : dat.strftime("%Y-%m-%d"),
                'inactive' : False if dat.month == month else True,
            })
                                                                                                                                                                                
        weeks.append(week)
        # iterate or leave
        if last_week_day.month != month:
            break
        else:
           first_week_day += dt.timedelta(days=7)


    context = {
        "prev_month" : (current_date - dt.timedelta(days=30)).strftime("%Y-%m-%d"),
        "next_month" : (current_date + dt.timedelta(days=30)).strftime("%Y-%m-%d"),
        "form" : CalendarForm(initial={'date_field': current_date}),
        "current_date" : current_date,
        "month_text" : current_date.strftime("%B"),
        "year_num" : year,
        "month_num" : month,
        "day_num" : current_date.day,
        "weekdays" : WEEKDAYS,
        "weeks" : weeks,
        "months" : get_months(current_date),
        "years" : get_years(current_date),
        "today" : TODAY(),
    }


    return render(request, template, context)

