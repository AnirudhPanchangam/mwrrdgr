
from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name = 'approvalView'),
	path('<int:object_id>/', views.pending, name='pending'),
	path('<int:object_id>/approved', views.approved, name='approve'),
	path('<int:object_id>/reval', views.reval, name='reval'),
	
]