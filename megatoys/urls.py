from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [	
	path('', 	   		   include('baseapp.urls')),
	path('profile/', 	   include('authapp.urls')),
	path('catalog/', 	   include('goodapp.urls')),
	path('cart/', 	   	   include('cartapp.urls')),
    path('admin/', admin.site.urls),
]
