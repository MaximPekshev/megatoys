from django.contrib import admin
from .models import Good, Picture


class PictureInline(admin.TabularInline):
    model = Picture
    exclude = ('title', 'slug','image420', 'image174')
    extra = 0

class GoodAdmin(admin.ModelAdmin):
	list_display = (
					'name',
					'vendor_code', 
					'good_code',
					'price',
					'quantity',
					)
	
	inlines 	 = [PictureInline]

	exclude = ('slug',)

admin.site.register(Good, GoodAdmin)

class PictureAdmin(admin.ModelAdmin):
	list_display = (
					'slug', 
					'title',				
					)
	list_filter = (
					'good', 
					)
	exclude = ('slug', 'image420', 'image174')

admin.site.register(Picture, PictureAdmin)