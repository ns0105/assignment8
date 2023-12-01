from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Class_Number(request):
    return render(request, 'thirdapp/clnumber.html ')

def Class_Time(request):
    return render(request, 'thirdapp/cltime.html')


