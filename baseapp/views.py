from django.shortcuts import render,redirect
import requests
from datetime import datetime, timezone
from .models import RenewableData, RegisterComplaint, Employee
from .forms import RenewableDataForm, ConsumerForm, EmployeeForm, RegisterComplaintForm

# Create your views here.

def home(request):
    return render(request, 'baseapp/home.html')

def tilt_angle(lat, month):
    if lat >= 25 and lat <= 50:
        if month >=3 and month <=9:
            return (lat*0.93)-21
        else:
            return (lat*0.875)+19.2
    else:
        if month >=3 and month <=9:
            return lat-15.69
        else:
            return lat+15.32

def renewable(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=c1e713603caa4579c69bef931cfd49d4"
    form = RenewableDataForm()
    if request.method == 'POST':
        form = RenewableDataForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['Cityname'] # form.cleaned_data returns a dictionary of validated form input fieldsand their values
            wattage = form.cleaned_data['wattage']
            r = requests.get(url.format(city_name = new_city )).json()
            # check string.format() and response.json() in requests
            #print(r)
            #print(r.json()) # sometimes we can also use "import json" inbuilt library in python

            unix_sunrise_timestamp = r['sys']['sunrise']
            unix_sunset_timestamp = r['sys']['sunset']
            utc_sunrise_time = datetime.fromtimestamp(unix_sunrise_timestamp, timezone.utc)
            utc_sunset_time = datetime.fromtimestamp(unix_sunset_timestamp, timezone.utc)        
            local_sunrise_time = utc_sunrise_time.astimezone()
            local_sunset_time = utc_sunset_time.astimezone()
            avg_time = local_sunset_time - local_sunrise_time
            avg_time = avg_time.seconds/3600.0
            power = wattage * avg_time * 0.75
            lat = r['coord']['lat']
            month = datetime.now().month
            print(month,lat)
            TA = tilt_angle(lat,month)
            city_weather = {
                'city': new_city,
                'lat': r['coord']['lat'],
                'lon': r['coord']['lon'],
                'temperature': r['main']['temp'],
                'wind': r['wind']['speed'],
                'wind_deg': r['wind']['deg'],
                'pressure': r['main']['pressure'],
                'humidity': r['main']['humidity'],
                'icon': r['weather'][0]['icon'],
                'average':avg_time,
                'TA':TA,
                'wattage':wattage,
                'power':power,
            }
            context = {'weather_data' : city_weather, 'form':form}
            return render(request, 'baseapp/renewable.html', context)

            '''count = RenewableData.objects.filter(Cityname=new_city).count()
            if count == 0:
                r = requests.get(url.format(city_name = new_city)).json()
                if r['cod'] == 200: 
                    form.save()'''
    context = {'form':form}
    return render(request, 'baseapp/renewable.html',context)

def complaint(request):
    context = {}
    if request.method == "POST":
        context['data'] = RegisterComplaint.objects.filter(consumer_id=request.POST['consumer_id'])
        return render(request, 'baseapp/complaint.html', context)
    context['data'] = RegisterComplaint.objects.all()
    return render(request, 'baseapp/complaint.html', context)

def bill(request):
    return render(request, 'baseapp/bill.html')

def power_factor(request):
    return render(request, "baseapp/power_factor.html")



# def delete(request, city_name):
#     RenewableData.objects.get(name=city_name).delete()
#     return redirect('home')

def register(request):
    context = {}
    consumer_form = RegisterComplaintForm(request.POST or None)
    if consumer_form.is_valid():
        consumer = consumer_form.save()
        consumer.save()
        return redirect('complaint')
    context['form'] = consumer_form
    context['employee_data'] = Employee.objects.all()
    return render(request, 'baseapp/register.html', context)

def employee_filter(request):
    context = {}
    consumer_form = RegisterComplaintForm()
    context['form'] = consumer_form
    if request.method == "POST":
        context['employee_data'] = Employee.objects.filter(area_code=request.POST['area_code'])
        return render(request, 'baseapp/register.html', context)

def things_speak(request):
    url = "http://api.thingspeak.com/channels/1352086/feed.json?key=WKOYCCHJYBPS32RO"
    data = requests.get(url).json()
    print(data)
    return redirect('home')