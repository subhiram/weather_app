from django.shortcuts import render, HttpResponse
import requests
from django.contrib import messages

# Create your views here.

def get_city(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = "https://weatherapi-com.p.rapidapi.com/current.json"

        querystring = {"q": city}

        headers = {
            "X-RapidAPI-Key": "95188b0615msh4ea7c3a1a7e8b6fp13c35ejsnfdc53d25fb2e",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }
        try:
            response = requests.get(url, headers=headers, params=querystring).json()
            b = response['current']['last_updated']
            time = b[-5] + b[-4] + b[-3] + b[-2] + b[-1]
            context = {
                'city': response['location']['name'],
                "time": time,
                "degree": response['current']['temp_c'],
                "condition": response['current']['condition']['text'],
                #"link": "https:"+response['current']['condition']['icon'],
                "wind": response['current']['wind_kph'],
                "humidity": response['current']['humidity'],
            }
            return render(request, 'weather_page.html', context=context)
        except:
            messages.info(request, "please enter a valid city name")
            return render(request, 'city_input.html')

    return render(request, 'city_input.html')

def city(request):
    if request.method == "POST":
        city = request.POST['city']
        print("this is the second function")
        print(city)
    return render(request, 'city_input.html')