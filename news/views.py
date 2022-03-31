from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def news_of_day(request):
    date = dt.date.today()
    day = convert_dates(date)
    return render(request, 'all-news/today-news.html', {"date":date,})


def convert_dates(dates):
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
    return days[day_number]


def past_days_news(request,past_date):
    # Converts data from the string Url
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
    
    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-news/past-news.html', {"date":date})
