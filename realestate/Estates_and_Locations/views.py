from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Estate_status, Estate_type, City, Estate
# Create your views here.

def main_page(request):
    estates = Estate_status.objects.all()
    type = Estate_type.objects.all()
    city = City.objects.all()
    filtered_estates = Estate.objects.all()
    template = loader.get_template('main.html')
    type_id = request.GET.get('type')
    status_id = request.GET.get('status')
    city_id = request.GET.get('city')  
    
    if type_id:
        filtered_estates = filtered_estates.filter(estate_type_id=type_id)
    elif status_id:
        filtered_estates = filtered_estates.filter(estate_status_id = status_id)
    elif city_id:
        filtered_estates = filtered_estates.filter(city_id = city_id)
    context = {
        'estates' : estates,
        'type' : type,
        'city' : city,
        'filtered_estates' : filtered_estates
    }
    return HttpResponse(template.render(context, request))

# def estate(request):
#     estates = Estate_status.objects.all()
#     template = loader.get_template('main.html')
#     context = {
#         'estates' : estates,
#     }
#     return HttpResponse(template.render(context, request))

def options(request):
    # Connect to database
    template = loader.get_template("index.html")
    # context = {}
    return HttpResponse(template.render())

def details(request):
    # Connect to db
    template = loader.get_template("details.html")
    # context = {}
    return HttpResponse(template.render())

