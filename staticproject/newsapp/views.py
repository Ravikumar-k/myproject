from django.shortcuts import render

# Create your views here.
def news(request):
    return render(request,'newsapp/news.html')

info1='good movie'
info2='worth watching'
info3='interesting sport'
info4='playing is good for health'
info5='jobs are always same'
info6='there are many jobs available in market'
def movies(request):
    return render(request,'newsapp/movies.html',{'info1':info1,'info2':info2})
def sports(request):
    return render(request,'newsapp/sports.html',{'info3':info3,'info4':info4})
def job(request):
    return render(request,'newsapp/jobs.html',{'info5':info5,'info6':info6})