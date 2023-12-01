from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app(request):
    return render(request, 'firstapp/welcome.html', {'fapp': 23, 'life': 'Water'})
def My_Identity(request):
    name = 'Nayema Sultana'
    home_district = 'Cumilla'
    country = 'Bangladesh'
    nationality = 'Bangladeshi'
    mother_Tounge = 'Bangla'
    identityDetails = {'a1': name, 'a2': home_district, 'a3': country, 'a4': nationality, 'a5': mother_Tounge  } 
    return render(request, 'firstapp/myidentity.html', identityDetails )

def My_Hobby(request):
    hobbies = {'listOfHobbies': ['Learning', 'Writing', 'Sewing', 'Singing']}
    return render(request, 'firstapp/hobby.html', hobbies)

