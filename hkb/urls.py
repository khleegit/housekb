from django.urls import path
from . import views


urlpatterns = [
   # path('', views.login, name='login'),
  	path('', views.login, name='login'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('classification_list/', views.classification_list, name='classification_list'),
	path('payment/', views.payment, name='payment'),
]