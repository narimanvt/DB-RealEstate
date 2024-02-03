from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def Clients_and_Contacts(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def sign_in_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/sign_in.html", context={"sign_in_form":form})