from django.shortcuts import render

def show_index(request):

	return render(request, 'baseapp/index.html')

def show_about_us(request):

	return render(request, 'baseapp/about_us.html')

def show_manufacture(request):

	return render(request, 'baseapp/manufacture.html')	

def show_certificate(request):

	return render(request, 'baseapp/certificate.html')

def show_news(request):

	return render(request, 'baseapp/news.html')

def show_privacy_policy(request):

	return render(request, 'baseapp/privacy_policy.html')

def show_payment(request):

	return render(request, 'baseapp/payment.html')

def show_delivery(request):

	return render(request, 'baseapp/delivery.html')	

def show_guarantee(request):

	return render(request, 'baseapp/guarantee.html')

def show_help(request):

	return render(request, 'baseapp/help.html')	