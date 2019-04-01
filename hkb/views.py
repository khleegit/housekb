from django.shortcuts import render, get_object_or_404



def login(request):
	return render(request, 'hkb/login.html', {})


def index(request):
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# posts = Post.objects.all()
	return render(request, 'hkb/index.html', {})

def payment(request):
	return render(request, 'hkb/payment.html', {})

def dashboard(request):
    return render(request, 'hkb/dashboard.html', {})