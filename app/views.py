from django.shortcuts import render , HttpResponse
import environ

import requests
import datetime
env = environ.Env()
environ.Env.read_env()
WEATHER_API_KEY = env("WEATHER_API_KEY")



def home(request):
        
     city = request.POST.get("city", "").strip()  
     zip_code = request.POST.get("zip_code", "").strip()

     if len(city) >0 or len(zip_code)==6:
        if city:
            url  = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}'
        elif zip_code:
           url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code},IN&appid={WEATHER_API_KEY}'
        params = {'units':'metric'}

        data = requests.get(url, params=params).json()
        cod = data['cod']
        if cod==200:
           description = data['weather'][0]['description']
           icon = data['weather'][0]['icon']
           temp = data['main']['temp']
           pressure = data['main']['pressure']
           humidity = data['main']['humidity']
           name = data['name']
           speed = data['wind']['speed']
        

           day = datetime.date.today()

           return render (request ,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'zip_code':zip_code, 'pressure':pressure,'humidity':humidity,'name':name,'speed':speed , 'success': 1})
        else :
            return render(request,"index.html",{'message':'Enter the valid input','success':1})

     
     else:
         print("data true")
         return render(request,"index.html",{'message':'Enter City or Pincode','success':1})
         