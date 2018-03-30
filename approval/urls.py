
from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name = 'approvalView'),
	path('<int:object_id>/', views.pending, name='pending'),
	
]