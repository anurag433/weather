from django.shortcuts import render , HttpResponse

import requests
import datetime

def home(request):

    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'delhi'     
    
    url  = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ee91c2932fa3e6b8a44818fb810ed332'

    params = {'units':'metric'}

    data = requests.get(url, params=params).json()


    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    day = datetime.date.today()

    return render (request ,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city})