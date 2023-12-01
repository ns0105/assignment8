from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Html_Practice(request):
    return render(request, 'appforHTML/htmlpractice.html')