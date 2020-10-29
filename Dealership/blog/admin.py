from django.contrib import admin
from .models import Car, Image

class ImageInLine(admin.TabularInline): 
	model = Image 
	extra = 1

class CarAdmin(admin.ModelAdmin): 
	list_display = ('title', 'date_posted', 'sold')
	inlines = [ImageInLine]
	search_fields = ['title']

admin.site.register(Car, CarAdmin)