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
    filtering = Contract.objects.all()
    template = loader.get_template("property.html")

    type = request.GET.get('type')
    status_id = request.GET.get('status')
    city = request.GET.get('city') 

    if type:
        filtered_estates = filtered_estates.filter(estate_type_id=type)
    elif status_id:
        filtered_estates = filtered_estates.filter(estate_status_id=status_id)
    elif city:
        filtered_estates = filtered_estates.filter(city=city)
        

    state = request.GET.get('state')
    district = request.GET.get('district')
    no_bedroom = request.GET.get('bedroom')
    no_bathroom = request.GET.get('bathroom')
    no_balcony = request.GET.get('balcony')
    floor_space = request.GET.get('floor')
    payment = request.GET.get('payment')

    if state:
        filtered_estates = filtered_estates.filter(estate_status_id=state)
    elif district:
        filtered_estates = filtered_estates.filter(district=district)
    elif no_bedroom:
        filtered_estates = filtered_estates.filter(number_of_bedrooms=no_bedroom)
    elif no_bathroom:
        filtered_estates = filtered_estates.filter(number_of_bathrooms=no_bathroom)
    elif no_balcony:
        filtered_estates = filtered_estates.filter(number_of_balconies=no_balcony)
    elif floor_space:
        filtered_estates = filtered_estates.filter(floor_space=floor_space)
    elif payment:
        filtering = filtering.filter(payment_amount=payment)
    

    context = {
        'filtered_estates' : filtered_estates,
        'filtering' : filtering,
    }
    return HttpResponse(template.render(context, request))

def estate_form(request):
    # Connect to db
    template = loader.get_template("estateform.html")
    # context = {}
    return HttpResponse(template.render())

