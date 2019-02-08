# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.test import Client

from django.urls import reverse

from . forms import *

from django.contrib.admin.sites import AdminSite

from django.contrib.admin.options import ModelAdmin

from . models import Customer,Hotel,Review

from . admin import Customer,Hotel,Review

from views import signin

# Create your tests here.

'----Django Test Cases For Forms----'

'----Customer Form----'

class Setup_Class(TestCase):
	def setUp(self):
		self.customer = Customer.objects.create(name="harshitha",username="harshi@example.com",password="harshi",confirm_password="harshi",area="Mylapore",house_number=1,street_name="1st Main Road",Landmark="Ground",Pincode=600028,State="TN",contact=9940642582,cuisine="Veg")

class Customer_Form_Test(TestCase):
	def test_CustomerForm_valid(self):
		form = CustomerForm(data={'name':"harshitha",'username':"harshi@example.com",'password':"harshi",'confirm_password':"harshi",'area':"Mylapore",'house_number':1,'street_name':"1st Main Road",'Landmark':"Ground",'Pincode':'600028','State':"TN",'contact':'9940642582','cuisine':'Veg'})
		self.assertTrue(form.is_valid())

	def test_CustomerForm_invalid(self):
		form = CustomerForm(data={'name':"harshitha",'username':"harshitha@example.com",'password':"harshi1308",'confirm_password':"harshi",'house_number':1,'street_name':"1st Main Road",'Landmark':"Ground",'Pincode':'600028','State':"TN",'contact':'9940642582'})
		self.assertFalse(form.is_valid())

'----Login Form----'

class Setup_Class(TestCase):
	def setUp(self):
		self.customer = Customer.objects.create(username="harshi@example.com",password="harshi")

class Login_Form_Test(TestCase):
	def test_LoginForm_valid(self):
		form = LoginForm(data={'username':"harshi@example.com",'password':"harshi"})
		self.assertTrue(form.is_valid())

	def test_LoginForm_invalid(self):
		form = LoginForm(data={'password':"harshi"})
		self.assertFalse(form.is_valid())

'----Review Form----'
class Setup_Class(TestCase):
	def setUp(self):
		self.customer = Review.objects(name="harshitha",Hotel_rating="*****",Hotel_review="Good")

class Review_Form_Test(TestCase):
	def test_ReviewForm_valid(self):
		form = ReviewForm(data={'name':"harshitha",'Hotel_rating':"*****",'Hotel_review':"Good"})
		self.assertTrue(form.is_valid())

	def test_ReviewForm_invalid(self):
		form = ReviewForm(data={'Rate_us':"*****"})
		self.assertFalse(form.is_valid())

'----Signup Form----'

class Setup_Class(TestCase):
	def setUp(self):
		self.customer = Customer.objects.create(name="harshitha",username="harshi@example.com",password="harshi1308",confirm_password="harshi",area="Mylapore",house_number=1,street_name="1st Main Road",Landmark="Ground",Pincode=600028,State="TN",contact=9940642582,cuisine="Veg")

class Signup_Form_Test(TestCase):
	def test_SignupForm_valid(self):
		form = SignupForm(data={'name':"harshitha",'username':"harshi@example.com",'password':"harshi1308",'confirm_password':"harshi",'area':"Mylapore",'house_number':1,'street_name':"1st Main Road",'Landmark':"Ground",'Pincode':'600028','State':"TN",'contact':'9940642582','cuisine':'Veg'})
		self.assertTrue(form.is_valid())

	def test_SignupForm_invalid(self):
		form = SignupForm(data={'username':"harshi@example.com",'password':"harshi1308",'house_number':1,'street_name':"1st Main Road",'Landmark':"Ground",'Pincode':'600028','State':"TN",'contact':'9940642582'})
		self.assertFalse(form.is_valid())



'----Django Test Cases For Models----'

'----Customer Model----'

class CustomerTestCase(TestCase):
	def setUp(self):
		Customer.objects.create(name="harshitha",username="harshitha@example.com",password="harshi1308",confirm_password="harshi",area="Mylapore",house_number=1,street_name="1st Main Road",Landmark="Ground",Pincode=600028,State="TN",contact=9940642582)
		Customer.objects.create(name="shreyas",username="shreyas@example.com",password="shreyas1309",confirm_password="shreyas1309",area="Banglore",house_number=2,street_name="3rd Main Road",Landmark="park",Pincode=600029,State="KA",contact=9940642592)
	
	def test_customer_model(self):
		harshitha = Customer.objects.get(name="harshitha")
		shreyas = Customer.objects.get(name="shreyas")
		self.assertEqual(harshitha.name,"harshitha")
		self.assertNotEqual(shreyas.name,"KA")
		self.assertNotEqual(harshitha.password,"KA")
		self.assertEqual(shreyas.password,"shreyas1309")

'----Review----'

class ReviewTestCase(TestCase):
	def setUp(self):
		Review.objects.create(name="harshitha",Hotel_rating="*****",Hotel_review="Good")

	def test_review_model(self):
		review = Review.objects.get(name="harshitha")
		self.assertNotEqual(review.name,"*****")
		self.assertEqual(review.Hotel_rating,"*****")


'----TestCases For Django Admin----'

class ModelAdminTest(TestCase):
	def setUp(self):
		self.review = Review.objects.create(name="harshitha",Hotel_rating="*****",Hotel_review="Good")
		self.site = AdminSite()

	def test_modeladmin_site(self):
		foods = ModelAdmin(Review,self.site)
		self.assertEqual(str(foods),'foods.ModelAdmin')


'Django Test Case For Views'
# class ViewsTestCase(Setup_Class):
# 	def test_displayhotels(self):
# 		response = self.client.get("/hotels/")
# 		self.assertNotEqual(response.status_code,400)

# 	def test_review(self):
# 		response = self.client.get("/review/")
# 		self.assertEqual(response.status_code,200)

class ViewsTestCase(Setup_Class):
	def test_displayhotels(self):
		hotels = self.client.login(username="harshi@example.com",password="harshi")
		self.assertTrue(hotels)
		response = self.client.get("/hotels/")
		self.assertEqual(response.status_code,400)
       	








