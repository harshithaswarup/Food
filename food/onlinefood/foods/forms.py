from django import forms
from models import Customer,Hotel,Food,Review
# 

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = "__all__"

'--Form for Login/Signing into the app--'

class LoginForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ("username","password")

'--Form for Signup--' 
'--(new member can create an account)--'

class SignupForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = "__all__"

'--Form for giving customer review--'
		
class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ("name","Hotel_rating","Hotel_review")

class HotelForm(forms.ModelForm):
	class Meta:
		model = Hotel
		fields = "__all__"
