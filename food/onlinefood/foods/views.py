# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.http import HttpResponseRedirect

from . models import Customer,Hotel,Food
# ,Review
from django import forms

from foods.forms import LoginForm,SignupForm,ReviewForm,HotelForm

from django.contrib import messages

#

# Create your views here.
'''--The view is for Login/Sign-in Page--
   The Username and Paswword fields are validated
   The Username and Passwprd will get stored in the DB'''

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			customer = Customer(username = username,password =password)
			username = Customer.objects.filter(username=username)
			password = Customer.objects.filter(password=password)
			if username.exists and password.exists():
				return render(request,'select.html',{'form':form,'username':username,'password':password})
			else:
				messages.warning(request,"Invalid Credentials ! Check Username and Password..!")
				return HttpResponseRedirect('')
	else:
		form = LoginForm()
	return render(request,'log_in.html',{'form':form})

'--This view is for Sign-up page--'
'--If not a member, the user can sign up--'
	

def signin(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			confirm_password = form.cleaned_data['confirm_password']
			customer = Customer(username=username,password=password,confirm_password=confirm_password)
			username = Customer.objects.filter(username=username)
			password = Customer.objects.filter(password=password)
			confirm_password = Customer.objects.filter(confirm_password=confirm_password)
			if username.exists():
				messages.warning(request,"Username aldready exists..")
			elif (password != confirm_password):
					messages.warning(request,"Password Mismatch")
			else:
				form.save()
				return render(request,'log_in.html',{'form':form})
	else:
		form = SignupForm()
	return render(request,'signup.html',{'form':form})
	
'--This view is for Displaying the list of hotels from the DB--'

def displayhotels(request):
	hotel = Hotel.objects.all()
	return render(request,'hotel_list.html',{'hotel':hotel})
			
'--This view is for displaying the food list from the DB--'

def displayfood(request,id):
	# import pdb;pdb.set_trace()
	hotel = Hotel.objects.get(id=id)
	foods = Food.objects.filter(hotel_name=hotel)
	return render(request,'food.html',{'foods':foods})

'--This view is for the review page--'

def review(request):
	if request.method == "POST":
		form = ReviewForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'last.html',{'form':form})
	else:
		form = ReviewForm()
	return render(request,'review.html',{'form':form})






