from django.shortcuts import render
import pygal
from input.models import SurfaceWaterData
from retrieve.forms import ListOfParams,ListOfAttr,FormForPdf
from django.template.loader import render_to_string
from pygal.style import DefaultStyle,DarkSolarizedStyle
from weasyprint import HTML
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

import random
# Create your views here.


def index(request):
	if request.method == 'POST':	
		form = ListOfAttr(request.POST)
		if form.is_valid():
			water_body = form.cleaned_data['name_of_river']
			param = form.cleaned_data['parameters']
			print(param)
			line_chart = pygal.Line(fill=True, interpolate='cubic', style=DefaultStyle) 
			obj2 = SurfaceWaterData.objects.filter(water_body_name = water_body).order_by('-date').values_list('date',flat=True)
			for i in range(0,len(param)):

				obj  = SurfaceWaterData.objects.filter(water_body_name = water_body).order_by('-date').values_list(param[i],flat=True)
				line_chart.add(param[i], obj )
			

			                                 
			line_chart.title = 'Plot of attributes against time '
			line_chart.x_labels = obj2
			
			chart = line_chart.render_data_uri()  
			return render(request,'retrieve/chart.html',{"chart":chart}) 
	form = ListOfAttr()
	return render(request,'retrieve/form_chart.html',{"form":form})


def view(request):
	if  request.method == 'POST':
		form = ListOfParams(request.POST)
		
		if form.is_valid():
			year = form.cleaned_data['year']
			water_body = form.cleaned_data['name_of_river']
			obj  = SurfaceWaterData.objects.filter(date__year = year,water_body_name = water_body).order_by('-date')
			return render(request,'retrieve/view.html',{"obj":obj,"year":year,"name":water_body})
	form = ListOfParams()
	return render(request,'retrieve/form.html',{"form":form})


def map_view(request):
	return render(request,'retrieve/maps.html')


def chart_temp(request):
	# labels = ["red","blue","green","yello","orange","white","brown"]
	# data_list = [{ 
 #        "data": [86,114,106,106,107,111,133,221,783,2478],
 #        "label": "Africa",
 #        "borderColor": "#3e95cd",
 #        # "fill": false
 #      }, { 
 #        "data": [282,350,411,502,635,809,947,1402,3700,5267],
 #        "label": "Asia",
 #        "borderColor": "#8e5ea2",
 #        # "fill": false
 #      }, { 
 #        "data": [168,170,178,190,203,276,408,547,675,734],
 #        "label": "Europe",
 #        "borderColor": "#3cba9f",
 #        # "fill": false
 #      }, { 
 #        "data": [40,20,10,16,24,38,74,167,508,784],
 #        "label": "Latin America",
 #        "borderColor": "#e8c3b9",
 #        # "fill": false
 #      }, { 
 #        "data": [6,3,2,2,7,26,82,172,312,433],
 #        "label": "North America",
 #        "borderColor": "#c45850",
 #        # "fill": false
 #      }
 #    ]


	if request.method == 'POST':	
		form = ListOfAttr(request.POST)
		if form.is_valid():
			r = lambda: random.randint(0,255)
			data_list = []
			water_body = form.cleaned_data['name_of_river']
			param = form.cleaned_data['parameters']
			print(param)
			# line_chart = pygal.Line(fill=True, interpolate='cubic', style=DefaultStyle) 
			labels = SurfaceWaterData.objects.filter(water_body_name = water_body).order_by('-date').values_list('date',flat=True)
			labels_final = []
			for i in range(0,len(labels)):
				labels_final.append(str(labels[i]))
			for i in range(0,len(param)):
				color = "%06x" % random.randint(0, 0xFFFFFF)
				obj  = SurfaceWaterData.objects.filter(water_body_name = water_body).order_by('-date').values_list(param[i],flat=True)
				# line_chart.add(param[i], obj )
				data_list.append(
					{
					"data":list(obj),
					"label":param[i],
					"borderColor": "#" + str(color),
					"fillColor": "#" + str(color),

					}


					)

			

			# data_list = [1,2,3,4,5] 
			return render(request,'retrieve/chart_template.html',{"data_list":data_list,"labels":labels_final}) 
	form = ListOfAttr()
	return render(request,'retrieve/form_chart.html',{"form":form})
	

def render_to_pdf(request):
	if request.method == 'POST':
		form = FormForPdf(request.POST)
		if form.is_valid():
			year_beg = form.cleaned_data['year_beg']
			year_end = form.cleaned_data['year_end']
			water_body = form.cleaned_data['name_of_river']
			obj  = SurfaceWaterData.objects.filter(date__year__range=[year_beg, year_end],water_body_name = water_body).order_by('-date')
			html_string = render_to_string('retrieve/pdf_template3.html',{"obj":obj,"year":year_end,"name":water_body})
			html = HTML(string=html_string, base_url=request.build_absolute_uri())
			html.write_pdf(target='/tmp/mypdf.pdf')
			fs = FileSystemStorage('/tmp')
			with fs.open('mypdf.pdf') as pdf:
				response = HttpResponse(pdf, content_type='application/pdf')
				#response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
				return response
				




	form = FormForPdf()
	return render(request,'retrieve/pdf_form.html',{"form":form})


def getdata(ob,label):
	datapoint = []
	for i in range(0,len(ob)):
		datapoint.append(
			{

			"x":label[i],
			"y":ob[i],
			"label":label[i],

			}


			)
	return datapoint



def render_to_chart(request):
	if request.method == 'POST':

		form = ListOfAttr(request.POST)
		if form.is_valid():
			r = lambda: random.randint(0,255)
			data_list = []
			water_body = form.cleaned_data['name_of_river']
			param = form.cleaned_data['parameters']
			print(param)
			# line_chart = pygal.Line(fill=True, interpolate='cubic', style=DefaultStyle) 
			labels = SurfaceWaterData.objects.filter(water_body_name = water_body).order_by('-date').values_list('date',flat=True)
			labels_final = []
			for i in range(0,len(labels)):
				labels_final.append(str(labels[i]))

			for i in range(0,len(param)):
				color = "%06x" % random.randint(0, 0xFFFFFF)
				obj  = SurfaceWaterData.objects.filter(water_body_name = water_body).order_by('-date').values_list(param[i],flat=True)
				# line_chart.add(param[i], obj )
				data_list.append(

					{

						"type":"line",
						"axisYType": "secondary",
						"name":param[i],
						"showInLegend": "true",
						"markerSize": 0,
						"yValueFormatString": "$#,###k",
						"dataPoints": getdata(list(obj),labels_final) 		


					}


					)
		return render(request,"retrieve/chart_render.html",{"chart_data":data_list})
	form = ListOfAttr()
	return render(request,"retrieve/form_chart.html",{"form":form})