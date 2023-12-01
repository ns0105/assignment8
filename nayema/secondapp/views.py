from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Beautiful_Color(request):
    return render(request, 'secondapp/color.html')
def Sirat_Book(request):
    return render(request, 'secondapp/sirat.html')


