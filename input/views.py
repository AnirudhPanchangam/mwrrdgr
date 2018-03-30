from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML
from django.core.mail import send_mail,EmailMessage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pygal
from input.models import SurfaceWaterData,WaterData
from input.forms import WaterForm,WaterDataForm
from input.calc import calculateIndex
from decimal import Decimal
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.
def index(request):
	return render(request,'input/index.html')




def html_to_pdf_view(request):
	paragraphs = ['first paragraph', 'second paragraph', 'third paragraph','paragraph','paragraph','paragraph','paragraph','paragraph','paragraph','paragraph','paragraph','paragraph','paragraph','paragraph','paragraph']


	line_chart = pygal.Line()
	line_chart.title = 'Browser usage evolution (in %)'
	line_chart.x_labels = map(str, range(2002, 2013))
	line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
	line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
	line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
	line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
	#line_chart.render()
	line_chart.render_to_png('/home/anirudh/myproject/input/static/chart.svg')  
	
	html_string = render_to_string('input/pdf_template.html', {'paragraphs': paragraphs})


	html = HTML(string=html_string, base_url=request.build_absolute_uri())

	html.write_pdf(target='/tmp/mypdf.pdf')
	# subject = "hello"
	# message = "Hello Again from django"
	# from_email = 'clanguy111@gmail.com'
	# recipient_list = ['anirudhpanchangam@gmail.com']
	# send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user='clanguy111@gmail.com', auth_password='tdakgjerpbyjcwhv', connection=None, html_message=None)
	# email = EmailMessage()
	# email.auth_user = 'clanguy111@gmail.com'
	# email.auth_password = 'tdakgjerpbyjcwhv'
	# email.subject = subject
	# email.body = message
	# email.fail_silently=False
	# email.from_email = 'clanguy111@gmail.com'
	# email.to_email = ["anirudhpanchangam@gmail.com",]
	# attachment = open('/tmp/mypdf.pdf', 'rb')
	# email.attach('mypdf.pdf',attachment)
	# email.send()
	# attachment.close()
	fromaddr = "clanguy111@gmail.com"
	toaddr = "anirudhpanchangam@gmail.com"
	msg = MIMEMultipart()

	# storing the senders email address  
	msg['From'] = fromaddr
	 
	# storing the receivers email address 
	msg['To'] = toaddr
	 
	# storing the subject 
	msg['Subject'] = "Auto-generated PDF"
	 
	# string to store the body of the mail
	body = "PFA attachment of your requested pdf"
	 
	# attach the body with the msg instance
	msg.attach(MIMEText(body, 'plain'))
	 
	# open the file to be sent 
	filename = "mypdf.pdf"
	attachment = open("/tmp/mypdf.pdf", "rb")
	 
	# instance of MIMEBase and named as p
	p = MIMEBase('application', 'octet-stream')
	 
	# To change the payload into encoded form
	p.set_payload((attachment).read())
	 
	# encode into base64
	encoders.encode_base64(p)
	  
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	 
	# attach the instance 'p' to instance 'msg'
	msg.attach(p)
	 
	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)
	 
	# start TLS for security
	s.starttls()
	 
	# Authentication
	s.login(fromaddr, "tdakgjerpbyjcwhv")
	 
	# Converts the Multipart msg into a string
	text = msg.as_string()
	 
	# sending the mail
	s.sendmail(fromaddr, toaddr, text)
	 
	# terminating the session
	s.quit()
	

	fs = FileSystemStorage('/tmp')
	with fs.open('mypdf.pdf') as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		#response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
		return response

	return response

def is_member_private(user):
    return user.groups.filter(name='private_organization').exists()


def charts(request):
	return render(request,"input/chart.html",{"data":[400,800,900,1000,2000]})

@login_required(login_url='/login/')
@user_passes_test(is_member_private)
def datainput(request):
	form = WaterForm()
	if request.method == 'POST':
		form = WaterForm(request.POST)
		if form.is_valid():

			dissolved_oxygen = form.cleaned_data['dissolved_oxygen']
			ph_val = form.cleaned_data['ph_val']
			electrical_conductivity = form.cleaned_data['electrical_conductivity']
			total_dissolved_solids = form.cleaned_data['total_dissolved_solids']	
			total_alkalinity = form.cleaned_data['total_alkalinity']
			total_hardness  = form.cleaned_data['total_hardness']
			total_suspended_solids = form.cleaned_data['total_suspended_solids']
			calcium = form.cleaned_data['calcium']
			magnesium = form.cleaned_data['magnesium']
			chlorides = form.cleaned_data['chlorides']
			nitrate = form.cleaned_data['nitrate']
			sulphate = form.cleaned_data['sulphate']
			biological_oxygen_demand = form.cleaned_data['biological_oxygen_demand']
			water_body_name = form.cleaned_data['water_body_name']
			list_of_params = [dissolved_oxygen,ph_val,electrical_conductivity,total_dissolved_solids,total_alkalinity,
			total_hardness,total_suspended_solids,calcium,magnesium,chlorides,nitrate,
			sulphate,biological_oxygen_demand
			]
			dict_of_params = {
				'ph_val':ph_val,
				'electrical_conductivity':electrical_conductivity,
				'dissolved_oxygen':dissolved_oxygen,
				'total_dissolved_solids':total_dissolved_solids,
				'total_alkalinity':total_alkalinity,
				'total_hardness':total_hardness,
				'total_suspended_solids':total_suspended_solids,
				'calcium':calcium,
				'magnesium':magnesium,
				'chlorides':chlorides,
				'nitrate':nitrate,
				'sulphate':sulphate,
				'biological_oxygen_demand':biological_oxygen_demand,



			}

			lat = form.cleaned_data['lat']
			lon = form.cleaned_data['lon']
			date = form.cleaned_data['date']

			wd = SurfaceWaterDataTemp()
			wd.dissolved_oxygen = dissolved_oxygen
			wd.ph_val = ph_val
			wd.electrical_conductivity = electrical_conductivity
			wd.total_dissolved_solids = total_dissolved_solids
			wd.total_alkalinity = total_alkalinity
			wd.total_hardness = total_hardness
			wd.total_suspended_solids = total_suspended_solids
			wd.calcium = calcium
			wd.magnesium = magnesium
			wd.chlorides = chlorides
			wd.nitrate = nitrate
			wd.sulphate = sulphate
			wd.biological_oxygen_demand = biological_oxygen_demand
			wd.water_body_name = water_body_name
			wd.lat = lat
			wd.lon = lon
			wd.date = date
			#call calculateIndex Function to calculate index
			#wd.quality_index = calculateIndex(list_of_params)
			quality = Decimal(calculateIndex(dict_of_params))
			wd.quality_index = round(quality,2)
			wd.save()

			user = request.user
			wd.user.add(user)		
			wd.save()
			
		return redirect('/input/')	
		

	return render(request,'input/form.html',{"form":form})



def data_input(request):
	if request.method == 'POST':
		form = WaterDataForm(request.POST)
		if form.is_valid():
			lab_type = form.cleaned_data['lab_type']
			if lab_type == 'L1':
				temperautre = form.cleaned_data['temperautre']
				colour = form.cleaned_data['colour']
				odour = form.cleaned_data['odour']
				electrical_conductivity = form.cleaned_data['electrical_conductivity']
				ph_val = form.cleaned_data['ph_val']
				dissolved_oxygen = form.cleaned_data['dissolved_oxygen']
				
				date = form.cleaned_data['date']
				lat = form.cleaned_data['lat']
				lng = form.cleaned_data['lng']
				
				wd = WaterDataTemp()
				
				wd.temperautre = temperautre
				wd.colour = colour
				wd.electrical_conductivity = electrical_conductivity
				wd.odour
				wd.ph_val = ph_val
				wd.dissolved_oxygen = dissolved_oxygen
				
				wd.date = date
				wd.lat = lat
				wd.lng = lng

				user = request.user
				wd.user.add(user)
				wd.save()


			if lab_type == 'L2':
				temperautre = form.cleaned_data['temperautre']
				electrical_conductivity = form.cleaned_data['electrical_conductivity']
				ph_val = form.cleaned_data['ph_val']
				dissolved_oxygen = form.cleaned_data['dissolved_oxygen']
				biological_oxygen_demand = form.cleaned_data['biological_oxygen_demand']
				chemical_oxygen_demand = form.cleaned_data['chemical_oxygen_demand']
				sodium = form.cleaned_data['sodium']
				calcium = form.cleaned_data['calcium']
				magnesium = form.cleaned_data['magnesium']
				potassium = form.cleaned_data['potassium']
				iron = form.cleaned_data['iron']
				boron = form.cleaned_data['boron']
				carbonate = form.cleaned_data['carbonate']
				bicarbonate = form.cleaned_data['bicarbonate']
				fluoride = form.cleaned_data['fluoride']
				chlorides = form.cleaned_data['chlorides']
				sulphate = form.cleaned_data['sulphate']
				nitrate = form.cleaned_data['nitrate']
				nitrite = form.cleaned_data['nitrite']
				silicate = form.cleaned_data['silicate']
				phosphate = form.cleaned_data['phosphate']
				total_plate_count = form.cleaned_data['total_plate_count']
				total_coliform = form.cleaned_data['total_coliform']
				fecal_coliform = form.cleaned_data['fecal_coliform']
				e_coliform = form.cleaned_data['e_coliform']

				date = form.cleaned_data['date']
				lat = form.cleaned_data['lat']
				lng = form.cleaned_data['lng']

				wd = WaterDataTemp()

				wd.temperautre = temperautre
				wd.electrical_conductivity = electrical_conductivity
				wd.ph_val = ph_val
				wd.dissolved_oxygen = dissolved_oxygen
				wd.biological_oxygen_demand = biological_oxygen_demand
				wd.chemical_oxygen_demand = chemical_oxygen_demand
				wd.sodium = sodium
				wd.calcium = calcium
				wd.magnesium = magnesium
				wd.potassium = potassium 
				wd.iron = iron
				wd.boron = boron
				wd.carbonate = carbonate
				wd.bicarbonate = bicarbonate
				wd.fluoride = fluoride
				wd.chlorides = chlorides
				wd.sulphate = sulphate
				wd.nitrate = nitrate
				wd.nitrite = nitrite
				wd.silicate = silicate
				wd.phosphate = phosphate
				wd.total_plate_count = total_plate_count
				wd.coliform = total_coliform
				wd.fecal_coliform = fecal_coliform
				wd.e_coliform = e_coliform

				wd.date = date
				wd.lat = lat
				wd.lng = lng

				user = request.user
				wd.user.add(user)
				wd.save()


			if lab_type == 'L3':
				temperautre = form.cleaned_data['temperautre']
				electrical_conductivity = form.cleaned_data['electrical_conductivity']
				ph_val = form.cleaned_data['ph_val']
				dissolved_oxygen = form.cleaned_data['dissolved_oxygen']
				biological_oxygen_demand = form.cleaned_data['biological_oxygen_demand']
				chemical_oxygen_demand = form.cleaned_data['chemical_oxygen_demand']
				sodium = form.cleaned_data['sodium']
				calcium = form.cleaned_data['calcium']
				magnesium = form.cleaned_data['magnesium']
				potassium = form.cleaned_data['potassium']
				iron = form.cleaned_data['iron']
				boron = form.cleaned_data['boron']
				carbonate = form.cleaned_data['carbonate']
				bicarbonate = form.cleaned_data['bicarbonate']
				fluoride = form.cleaned_data['fluoride']
				chlorides = form.cleaned_data['chlorides']
				sulphate = form.cleaned_data['sulphate']
				nitrate = form.cleaned_data['nitrate']
				nitrite = form.cleaned_data['nitrite']
				silicate = form.cleaned_data['silicate']
				phosphate = form.cleaned_data['phosphate']
				total_plate_count = form.cleaned_data['total_plate_count']
				total_coliform = form.cleaned_data['total_coliform']
				fecal_coliform = form.cleaned_data['fecal_coliform']
				e_coliform = form.cleaned_data['e_coliform']
				total_organic_carbon = form.cleaned_data['total_organic_carbon']
				total_nitrogen = form.cleaned_data['total_nitrogen']
				total_kjeldhal_nitrogen = form.cleaned_data['total_kjeldhal_nitrogen']
				ammonia_nitrogen = form.cleaned_data['ammonia_nitrogen']
				cyanide = form.cleaned_data['cyanide']
				arsenic = form.cleaned_data['arsenic']
				cadmium = form.cleaned_data['cadmium']
				mercury = form.cleaned_data['mercury']
				chromium = form.cleaned_data['chromium']
				lead = form.cleaned_data['lead']
				zinc = form.cleaned_data['zinc']

				date = form.cleaned_data['date']
				lat = form.cleaned_data['lat']
				lng = form.cleaned_data['lng']

				wd = WaterDataTemp()

				wd.temperautre = temperautre
				wd.electrical_conductivity = electrical_conductivity
				wd.ph_val = ph_val
				wd.dissolved_oxygen = dissolved_oxygen
				wd.biological_oxygen_demand = biological_oxygen_demand
				wd.chemical_oxygen_demand = chemical_oxygen_demand
				wd.sodium = sodium
				wd.calcium = calcium
				wd.magnesium = magnesium
				wd.potassium = potassium 
				wd.iron = iron
				wd.boron = boron
				wd.carbonate = carbonate
				wd.bicarbonate = bicarbonate
				wd.fluoride = fluoride
				wd.chlorides = chlorides
				wd.sulphate = sulphate
				wd.nitrate = nitrate
				wd.nitrite = nitrite
				wd.silicate = silicate
				wd.phosphate = phosphate
				wd.total_plate_count = total_plate_count
				wd.coliform = total_coliform
				wd.fecal_coliform = fecal_coliform
				wd.e_coliform = e_coliform
				wd.total_organic_carbon = total_organic_carbon
				wd.total_nitrogen = total_nitrogen
				wd.total_kjeldhal_nitrogen = total_kjeldhal_nitrogen
				wd.ammonia_nitrogen = ammonia_nitrogen
				wd.cyanide = cyanide
				wd.arsenic = arsenic
				wd.cadmium = cadmium
				wd.mercury = mercury
				wd.chromium = chromium
				wd.lead = lead
				wd.zinc = zinc

				wd.date = date
				wd.lat = lat
				wd.lng = lng

				user = request.user
				wd.user.add(user)
				wd.save()

		return redirect('/')




	form = WaterDataForm()
	return render(request,'input/form1.html',{"form":form})