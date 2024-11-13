from django.shortcuts import render

# Create your views here.
def baseview(request):
    return render(request,'adv_app/base.html')
def sportsinfo(request):
    info1='good to play games'
    return render(request,'adv_app/sportsinfo.html',{'info1':info1})
def moviesinfo(request):
    info2='entertainment is necessary '
    return render(request,'adv_app/moviesinfo.html',{'info2':info2})
def jobsinfo(request):
    info3='jobs are best to earn money'
    return render(request,'adv_app/jobsinfo.html',{'info3':info3})