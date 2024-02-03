from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Estate_status, Estate_type, City, Estate
from Contracts_and_Transactions.models import Contract
# Create your views here.

def main_page(request):
    estates = Estate_status.objects.all()
    type = Estate_type.objects.all()
    city = City.objects.all()
    template = loader.get_template('main.html')
    context = {
        'estates' : estates,
        'type' : type,
        'city' : city,
    }
    return HttpResponse(template.render(context, request))


def property(request):
    filtered_estates = Estate.objects.all()
    city = City.objects.all()
    filtering = Contract.objects.all()
    estate_type = Estate_type.objects.all()
    estate_status = Estate_status.objects.all()
    template = loader.get_template("property.html")
    

    type = request.GET.get('type')
    status_id = request.GET.get('status')
    city_name = request.GET.get('city')
    district = request.GET.get('district') 
    districts = list(range(1,23)) #defining it for loop in the html part to avoid writing 22 options
    rooms = list(range(1,7))
    no_bedroom = request.GET.get('no_bedroom')
    no_bathroom = request.GET.get('no_bathroom')
    no_balcony = request.GET.get('no_balcony')
    floor_space = request.GET.get('floor_space')
    floor_space_output = request.GET.get('floor_space_output')
    payment = request.GET.get('payment')
    if type:
        filtered_estates = filtered_estates.filter(estate_type_id=type)
    elif status_id:
        filtered_estates = filtered_estates.filter(estate_status_id=status_id)
    elif city_name:
        filtered_estates = filtered_estates.filter(city=city_name)
    elif district:
        filtered_estates = filtered_estates.filter(district = district)
    elif no_bedroom:
        filtered_estates = filtered_estates.filter(number_of_bedrooms=no_bedroom)
    elif no_bathroom:
        filtered_estates = filtered_estates.filter(number_of_bathrooms=no_bathroom)
    elif no_balcony:
        filtered_estates = filtered_estates.filter(number_of_balconies=no_balcony)
    elif floor_space and floor_space_output != '0':
            filtered_estates = filtered_estates.filter(floor_space=floor_space)
        

    elif payment:
        filtering = filtering.filter(payment_amount=payment)        
        

    
    

    
   
    

    context = {
        'filtered_estates' : filtered_estates,
        'filtering' : filtering,
        'city' : city,
        'estate_type' : estate_type,
        'estate_status' : estate_status,
        'districts' : districts,
        'rooms' : rooms
    }
    return HttpResponse(template.render(context, request))

def estate_form(request):
    # Connect to db
    template = loader.get_template("estateform.html")
    # context = {}
    return HttpResponse(template.render())

def details(request):
    template = loader.get_template("details.html")
    return HttpResponse(template.render())
