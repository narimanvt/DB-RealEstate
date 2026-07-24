from django.http import HttpResponse
from django.template import loader
from .models import Contract, Transaction


def contract_list(request):
    template = loader.get_template('contracts.html')
    context = {'contracts': Contract.objects.select_related(
        'client', 'employee', 'estate', 'contract_type'
    ).all()}
    return HttpResponse(template.render(context, request))


def transaction_list(request):
    template = loader.get_template('transactions.html')
    context = {'transactions': Transaction.objects.select_related(
        'transaction_type', 'client_offered', 'client_requested'
    ).all()}
    return HttpResponse(template.render(context, request))
