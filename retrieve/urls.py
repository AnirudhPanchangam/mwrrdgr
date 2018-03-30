
from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name = 'index'),
	path('view/',views.view,name = 'view'),
	path('maps/',views.map_view,name = 'maps'),
	path('chart/',views.chart_temp,name = 'chart'),
	path('pdf/',views.render_to_pdf,name = 'pdf'),
	path('graph/',views.render_to_chart,name = 'graph'),

	
]