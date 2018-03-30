
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	path('',views.index,name = 'loginIndex'),
	path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout_user'),
]