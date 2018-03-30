
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	path('',views.index,name = 'inputIndex'),
	path('pdf/',views.html_to_pdf_view,name = 'ipdf'),
	path('chart/',views.charts,name = 'charts'),
	path('in/',views.datainput,name = 'get_input'),
	path('get/',views.data_input,name = 'input'),		
]