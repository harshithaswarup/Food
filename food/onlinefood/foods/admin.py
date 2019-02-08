# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Customer,Hotel,Food,Review
# 

# Register your models here.
'--This Stores all the data related to Hotel--'

admin.site.register(Hotel)

'--This stores all the data related to Food--'

admin.site.register(Food)

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('username','password')
admin.site.register(Customer,CustomerAdmin)

'''--This Stores the data related to review 
	Data entered by the customer in the feedback 
	form--'''

class ReviewAdmin(admin.ModelAdmin):
	list_display = ('name','Hotel_rating','Hotel_review')
admin.site.register(Review,ReviewAdmin)
