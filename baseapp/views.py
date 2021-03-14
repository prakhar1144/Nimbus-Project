from django.shortcuts import render,redirect
import requests
from .models import City
from .forms import Cityform

# Create your views here.

def home(request):
    return render(request, 'baseapp/home.html')

def renewable(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=c1e713603caa4579c69bef931cfd49d4"
   
    if request.method == 'POST':
        form = Cityform(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name'] # form.cleaned_data returns a dictionary of validated form input fieldsand their values
            count = City.objects.filter(name=new_city).count()
            if count == 0:
                r = requests.get(url.format(city_name = new_city)).json()
                if r['cod'] == 200: 
                    form.save()
    
    form = Cityform()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city_name = city)).json() 
        # check string.format() and response.json() in requests
        #print(r)
        #print(r.json()) # sometimes we can also use "import json" inbuilt library in python

        city_weather = {
            'city': city,
            'lat': r['coord']['lat'],
            'lon': r['coord']['lon'],
            'temperature': r['main']['temp'],
            'wind': r['wind']['speed'],
            'wind_deg': r['wind']['deg'],
            'pressure': r['main']['pressure'],
            'humidity': r['main']['humidity'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form':form}
    return render(request, 'baseapp/renewable.html', context)

def delete(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')