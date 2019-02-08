# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

'--Model for Customer--'

class Customer(models.Model):
	name = models.CharField(max_length=50,default="Rakhi")
	username = models.CharField(max_length=20,default="Enter username or registered phone number")
	password = models.CharField(max_length=10)
	confirm_password = models.CharField(max_length=10,default="harshi")
	area = models.CharField(max_length=100,default="R.A Puram")
	house_number = models.IntegerField(default=11/23)
	street_name = models.CharField(max_length=50,default="1st Main Road")
	Landmark = models.CharField(max_length=50,default="Near Billroth Hospital")
	Pincode = models.IntegerField(default=600028)
	State = models.CharField(max_length=50,default="TN")
	contact = models.CharField(null=False,blank=False,max_length=10,default=9940642582)
	
	
	class Meta:
		db_table = "Customer"

'--Model for Hotel--'

class Hotel(models.Model):
	logo = models.ImageField(upload_to="Desktop/",default='/static/food_gawker.jpg/')
	name = models.CharField(max_length=50,default="Drunken Monkey")
	area = models.CharField(max_length=50,default="Alwarpet")
	address = models.TextField(max_length=100,default="address")
	phone = models.IntegerField(default=1233)
	approximate_cost = models.IntegerField(default=350)
	special_food = models.CharField(max_length=50,default="Willi Wonka")
	

	class Meta:
		db_table = "Hotel"

'--Model for Hotel--'
'certain fields are initiated with foreign keys'
'All food related fields are defined'

class Food(models.Model):
	image = models.ImageField(upload_to = 'media', default = 'ss/page12_signout.PNG')
	hotel_name = models.ForeignKey(Hotel,on_delete=models.CASCADE)
	hotel_description = models.CharField(max_length=500,default="Enter description")
	rate = models.CharField(max_length=5,default='*****')
	min_time = models.CharField(max_length=50,default="20 mins")
	cost = models.IntegerField()

	
	class Meta:
		db_table = "Food"

'--Model for Review--'	

class Review(models.Model):
	# name = models.ForeignKey(Customer,on_delete=models.CASCADE)
	name = models.CharField(max_length=20,default="Harshi")
	Hotel_rating = models.CharField(max_length=5,default="Rate")
	Hotel_review = models.CharField(max_length=100,default="Good")

	class Meta:
		db_table = "Review"
			

