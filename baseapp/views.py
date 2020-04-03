from django.shortcuts import render
from cartapp.views import get_cart

def show_index(request):

	context = {'cart_summ': (get_cart(request).summ if get_cart(request) else 0),}

	return render(request, 'baseapp/index.html', context)

def show_about_us(request):

	context = {'cart_summ': (get_cart(request).summ if get_cart(request) else 0),}

	return render(request, 'baseapp/about_us.html', context)

def show_manufacture(request):

	context = {'cart_summ': (get_cart(request).summ if get_cart(request) else 0),}
	return render(request, 'baseapp/manufacture.html', context)	

def show_certificate(request):

	context = {'cart_summ': (get_cart(request).summ if get_cart(request) else 0),}
	return render(request, 'baseapp/certificate.html', context)

def show_news(request):

	context = {'cart_summ': (get_cart(request).summ if get_cart(request) else 0),}
	return render(request, 'baseapp/news.html', context)

def show_privacy_policy(request):

	context = {'cart_summ': (get_cart(request).summ if get_cart(request) else 0),}
	return render(request, 'baseapp/privacy_policy.html', context)

def show_payment(request):

	context = {'cart_summ': (get_cart(request).summ if get_cart(request) else 0),}
	return render(request, 'baseapp/payment.html', context)

def show_delivery(request):

	context = {'cart_summ': (get_cart(request).summ if get_cart(request) else 0),}
	return render(request, 'baseapp/delivery.html', context)	

def show_guarantee(request):

	context = {'cart_summ': (get_cart(request).summ if get_cart(request) else 0),}
	return render(request, 'baseapp/guarantee.html', context)

def show_help(request):
	
	context = {'cart_summ': (get_cart(request).summ if get_cart(request) else 0),}
	return render(request, 'baseapp/help.html', context)	