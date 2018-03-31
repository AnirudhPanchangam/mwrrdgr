from django.shortcuts import render
from input.models import WaterDataTemp,WaterData
from input.forms import WaterDataForm
# Create your views here.



def index(request):
	approval_list = WaterDataTemp.objects.filter(flag = 1).order_by('-date')


	context = {
	
	"approval_list":approval_list,
	
	}
	return render(request,'approval/index.html',{"approval_list":approval_list})

def pending(request,object_id):
	pending_data = WaterDataTemp.objects.filter(pk = object_id)
	return render(request,'approval/pending.html',{"pending_data":pending_data})


def approved(request,object_id):

	approved_data = WaterDataTemp.objects.filter(pk = object_id)
	wd = WaterData()
	if approved_data.laboratory == 'L2':
		wd.temperature = approved_data.temperautre
		wd.electrical_conductivity = approved_data.electrical_conductivity
		wd.ph_val = approved_data.ph_val
		wd.dissolved_oxygen = approved_data.dissolved_oxygen
		wd.biological_oxygen_demand = approved_data.biological_oxygen_demand
		wd.chemical_oxygen_demand = approved_data.chemical_oxygen_demand
		wd.sodium = approved_data.sodium
		wd.calcium = approved_data.calcium
		wd.magnesium = approved_data.magnesium
		wd.potassium = approved_data.potassium 
		wd.iron = approved_data.iron
		wd.boron = approved_data.boron
		wd.carbonate = approved_data.carbonate
		wd.bicarbonate = approved_data.bicarbonate
		wd.fluoride = approved_data.fluoride
		wd.chlorides = approved_data.chlorides
		wd.sulphate = approved_data.sulphate
		wd.nitrate = approved_data.nitrate
		wd.nitrite = approved_data.nitrite
		wd.silicate = approved_data.silicate
		wd.phosphate = approved_data.phosphate
		wd.total_plate_count = approved_data.total_plate_count
		wd.coliform = approved_data.total_coliform
		wd.fecal_coliform = approved_data.fecal_coliform
		wd.e_coliform = approved_data.e_coliform

		wd.date = approved_data.date
		wd.lat = approved_data.lat
		wd.lng = approved_data.lng

		wd.water_body_name = approved_data.water_body_name

		wd.user.add(request.user)
		wd.save()

	if approved_data.laboratory == 'L1':
		
		wd.temperature = approved_data.temperautre
		wd.colour = approved_data.colour
		wd.electrical_conductivity = approved_data.electrical_conductivity
		wd.odour = approved_data.odour
		wd.ph_val = approved_data.ph_val
		wd.dissolved_oxygen = approved_data.dissolved_oxygen
			

		wd.date = approved_data.date
		wd.lat = approved_data.lat
		wd.lng = approved_data.lng

		wd.water_body_name = approved_data.water_body_name

		wd.user.add(request.user)
		wd.save()

	if approved_data.laboratory == 'L3':
		
		wd.temperature = approved_data.temperautre
		wd.electrical_conductivity = approved_data.electrical_conductivity
		wd.ph_val = approved_data.ph_val
		wd.dissolved_oxygen = approved_data.dissolved_oxygen
		wd.biological_oxygen_demand = approved_data.biological_oxygen_demand
		wd.chemical_oxygen_demand = approved_data.chemical_oxygen_demand
		wd.sodium = approved_data.sodium
		wd.calcium = approved_data.calcium
		wd.magnesium = approved_data.magnesium
		wd.potassium = approved_data.potassium 
		wd.iron = approved_data.iron
		wd.boron = approved_data.boron
		wd.carbonate = approved_data.carbonate
		wd.bicarbonate = approved_data.bicarbonate
		wd.fluoride = approved_data.fluoride
		wd.chlorides = approved_data.chlorides
		wd.sulphate = approved_data.sulphate
		wd.nitrate = approved_data.nitrate
		wd.nitrite = approved_data.nitrite
		wd.silicate = approved_data.silicate
		wd.phosphate = approved_data.phosphate
		wd.total_plate_count = approved_data.total_plate_count
		wd.coliform = approved_data.total_coliform
		wd.fecal_coliform = approved_data.fecal_coliform
		wd.e_coliform = approved_data.e_coliform
		wd.total_organic_carbon = approved_data.total_organic_carbon
		wd.total_nitrogen = approved_data.total_nitrogen
		wd.total_kjeldhal_nitrogen = approved_data.total_kjeldhal_nitrogen
		wd.ammonia_nitrogen = approved_data.ammonia_nitrogen
		wd.cyanide = approved_data.cyanide
		wd.arsenic = approved_data.arsenic
		wd.cadmium = approved_data.cadmium
		wd.mercury = approved_data.mercury
		wd.chromium = approved_data.chromium
		wd.lead = approved_data.lead
		wd.zinc = approved_data.zinc

		wd.date = approved_data.date
		wd.lat = approved_data.lat
		wd.lng = approved_data.lng

		wd.water_body_name = approved_data.water_body_name

		wd.user.add(request.user)
		wd.save()


	return render(request,'approval/approved.html',{})


def reval(request,object_id):
	temp_data = WaterDataTemp.objects.filter(pk = object_id)
	temp_data.reval_flag = 1
	return render(request,'approval/reval_sent.html')

def view_reval(request):
	reval_data = WaterDataTemp.objects.filter(reval_flag = 1)
	return render(request,'approval/reval.html',{"reval_data":reval_data})

def re_entry(request,object_id):
	if request.method == 'POST':
		form = WaterDataForm(request.POST)
		if form.is_valid():
			lab_type = form.cleaned_data['laboratory']
			if lab_type == 'lab1':
				temperature = form.cleaned_data['temperature']
				colour = form.cleaned_data['colour']
				odour = form.cleaned_data['odour']
				electrical_conductivity = form.cleaned_data['electrical_conductivity']
				ph_val = form.cleaned_data['ph_val']
				dissolved_oxygen = form.cleaned_data['dissolved_oxygen']
				
				date = form.cleaned_data['date']
				lat = form.cleaned_data['lat']
				lng = form.cleaned_data['lng']
				
				wd = WaterDataTemp.objects.filter(pk = object_id)
				
				wd.temperature = temperature
				wd.colour = colour
				wd.electrical_conductivity = electrical_conductivity
				wd.odour
				wd.ph_val = ph_val
				wd.dissolved_oxygen = dissolved_oxygen
				
				wd.date = date
				wd.lat = lat
				wd.lng = lng
				wd.flag = 1

				user = request.user
				
				wd.save()
				wd.user.add(user)

			if lab_type == 'lab2':
				temperature = form.cleaned_data['temperature']
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

				wd = WaterDataTemp.objects.filter(pk = object_id)
				
				wd.temperature = temperature
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
				wd.water_body_name = form.cleaned_data['water_body_name']
				wd.date = date
				wd.lat = lat
				wd.lng = lng
				wd.flag = 1

				user = request.user
				
				wd.save()
				wd.user.add(user)

			if lab_type == 'lab3':
				temperature = form.cleaned_data['temperature']
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

				wd.water_body_name = form.cleaned_data['water_body_name']

				date = form.cleaned_data['date']
				lat = form.cleaned_data['lat']
				lng = form.cleaned_data['lng']

				wd = WaterDataTemp.objects.filter(pk = object_id)

				wd.temperature = temperature
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

				wd.water_body_name = form.cleaned_data['water_body_name']

				wd.date = date
				wd.lat = lat
				wd.lng = lng
				wd.flag = 1
				user = request.user
				
				wd.save()
				wd.user.add(user)
			return redirect('/')
		print(form.errors)
		return redirect('/get')




	form = WaterDataForm()
	return render(request,'input/param_all.html',{"form":form}) #param_all
