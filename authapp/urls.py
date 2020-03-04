from django.urls import path
from .views import login_register, show_account
from .views import login, logout, registration

urlpatterns = [	
	path('',					show_account, name='show_account'),
	path('login-register/',		login_register, name='login_register'),
	path('login/',				login, name='login'),
	path('logout/',				logout, name='logout'),
	path('registration/',		registration, name='registration'),
]
