from django.http import HttpResponse
from django.template import loader
from .models import Client, Employee


def client_list(request):
    template = loader.get_template('clients.html')
    context = {'clients': Client.objects.all()}
    return HttpResponse(template.render(context, request))


def employee_list(request):
    template = loader.get_template('employees.html')
    context = {'employees': Employee.objects.all()}
    return HttpResponse(template.render(context, request))
