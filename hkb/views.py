from django.shortcuts import render, get_object_or_404
from .models import Classification


def login(request):
	return render(request, 'hkb/login.html', {})


def dashboard(request):
	return render(request, 'hkb/dashboard.html', {})

def classification_list(request):
	total_list = Classification.objects.all()
	return render(request, 'hkb/classification_list.html', {'total_list':total_list})

def payment(request):
	return render(request, 'hkb/payment.html', {})
