from django.shortcuts import render , HttpResponse

import requests
import datetime

def home(request):

    if 'city' in requests.POST:
        city = request.POST['city']

    else :
        city = 'Delhi'

    url  = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ee91c2932fa3e6b8a44818fb810ed332'

    PARAMS = {'units':'metric'}

    data = request.get(url,PARAMS).json()
    
    return render (request ,'index.html')