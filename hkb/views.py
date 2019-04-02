from django.shortcuts import render, get_object_or_404



def login(request):
	return render(request, 'hkb/login.html', {})


def dashboard(request):
	return render(request, 'hkb/dashboard.html', {})

def payment(request):
	return render(request, 'hkb/payment.html', {})
