from django.shortcuts 				import render, redirect

from django.http 					import HttpResponseRedirect

from django.contrib.auth.models		import User
from django.contrib.auth.forms 		import AuthenticationForm
from django.contrib					import messages

from django.contrib		 			import auth
from .forms 						import RegistrationForm
from authapp.models 				import Buyer

from cartapp.views 					import get_cart

def show_account(request):
	
	if request.user.is_authenticated:

		context = {'cart_summ': (get_cart(request).summ if get_cart(request) else 0),}

		template_name = 'authapp/profile.html'

		buyer = Buyer.objects.filter(user=request.user).first()
		
		if buyer is not None:
			
			context.append({'buyer': buyer})

		return render(request, template_name, context)
	else:
		return redirect('login_register')	


def login_register(request):

	context = {'cart_summ': (get_cart(request).summ if get_cart(request) else 0),}

	template_name = 'authapp/login_register.html'
	
	return render(request, template_name, context)

def login(request):

	if request.method == 'POST':
		form 			= AuthenticationForm(request, request.POST)

		username 		= form.data.get('username')
		password 		= form.data.get('password')

		user 			= auth.authenticate(username=username, password=password)

		if user is not None:

			auth.login(request, user)
			return redirect('show_account')

		else:
			messages.info(request, 'Вы ввели не существующую комбинацию пароль-логин, попробуйте еще раз!')
			return redirect('login_register')		
	else:
		return HttpResponseRedirect('/')

def logout(request):
	
	auth.logout(request)

	return redirect('login_register')


def registration(request):

	if request.method == 'POST':

		reg_form = RegistrationForm(request.POST)

		if reg_form.is_valid():

			userfirst_name 	= reg_form.cleaned_data['userfirst_name']
			userlast_name 	= reg_form.cleaned_data['userlast_name']
			username 		= reg_form.cleaned_data['username']
			useremail 		= reg_form.cleaned_data['useremail']
			userpassword 	= reg_form.cleaned_data['userpassword']
			userpassword_2 	= reg_form.cleaned_data['userpassword_2']

			if userpassword==userpassword_2:
				if User.objects.filter(username=username).exists():
					messages.info(request, 'Пользователь с таким именем существует!!!')
					return redirect('login_register')
				elif User.objects.filter(email=useremail).exists():				
					messages.info(request, 'Пользователь с таким email существует!!!')
					return redirect('login_register')
				else:
					user = User.objects.create_user(username=username, password=userpassword, email=useremail)
					user.save()

					new_buyer		= Buyer(user=user, first_name=userfirst_name, last_name=userlast_name)

					auth.login(request, user)

					template_name = 'baseapp/index.html'

					return render(request, template_name)	
			else:
				messages.info(request, 'Пароли не совпадают!!!')
				return redirect('login_register')
		else:

			return HttpResponseRedirect('/')					
	else:

		return HttpResponseRedirect('/')