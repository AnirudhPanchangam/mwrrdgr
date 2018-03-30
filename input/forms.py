from django import forms

from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import date


class WaterForm(forms.Form):
	dissolved_oxygen = forms.FloatField()  				 
	ph_val = forms.FloatField(
		validators = [MaxValueValidator(7),MinValueValidator(-7)]
			)
	electrical_conductivity = forms.FloatField()
	total_dissolved_solids = forms.FloatField()
	total_alkalinity = forms.FloatField()
	total_hardness = forms.FloatField()
	total_suspended_solids = forms.FloatField()
	calcium = forms.FloatField()
	magnesium = forms.FloatField()
	chlorides = forms.FloatField()
	nitrate = forms.FloatField()
	sulphate = forms.FloatField()
	biological_oxygen_demand = forms.FloatField()
	
	#data not related to quality
	water_body_name = forms.CharField(max_length = 140)
	lat = forms.FloatField()
	lon = forms.FloatField()
	
	
	date = forms.DateField(widget = forms.widgets.SelectDateWidget())


class WaterDataForm(forms.Form):
	dissolved_oxygen = forms.FloatField(required = False)  				 
	ph_val = forms.FloatField(
		validators = [MaxValueValidator(14),MinValueValidator(0)]
			)
	electrical_conductivity = forms.FloatField(required = False)
	total_dissolved_solids = forms.FloatField(required = False)
	total_alkalinity = forms.FloatField(required = False)
	total_hardness = forms.FloatField(required = False)
	total_suspended_solids = forms.FloatField(required = False)
	calcium = forms.FloatField(required = False)
	magnesium = forms.FloatField(required = False)
	chlorides = forms.FloatField(required = False)
	nitrate = forms.FloatField(required = False)
	sulphate = forms.FloatField(required = False)
	biological_oxygen_demand = forms.FloatField(required = False)
	quality_index = forms.FloatField(required = False)
	temperature = forms.FloatField(required = False)
	colour = forms.CharField(max_length = 25,required = False)
	odour = forms.IntegerField(required = False)
	chemical_oxygen_demand = forms.FloatField(required = False)
	iron = forms.FloatField(required = False)
	potassium = forms.FloatField(required = False)
	phosphate = forms.FloatField(required = False)
	nitrate = forms.FloatField(required = False)
	nitrite = forms.FloatField(required = False)
	boron = forms.FloatField(required = False)
	bicarbonate = forms.FloatField(required = False)
	fluoride = forms.FloatField(required = False)
	total_plate_count  = forms.FloatField(required = False)
	total_coliform = forms.FloatField(required = False)
	fecal_coliform = forms.FloatField(required = False)
	e_coliform = forms.FloatField(required = False)
	sodium = forms.FloatField(required = False)
	carbonate = forms.FloatField(required = False)
	silicate = forms.FloatField(required = False)
	total_organic_carbon = forms.FloatField(required = False)
	total_kjelhdal_nitrogen = forms.FloatField(required = False)
	ammonia_nitrogen = forms.FloatField(required = False)
	cyanide = forms.FloatField(required = False)
	arsenic = forms.FloatField(required = False)
	cadium = forms.FloatField(required = False)
	mercury = forms.FloatField(required = False)
	chromium = forms.FloatField(required = False)
	lead  = forms.FloatField(required = False)
	zinc = forms.FloatField(required = False)

	water_body_name = forms.CharField(max_length = 140)
	lat = forms.FloatField()
	lon = forms.FloatField()
	laboratory = forms.ChoiceField(choices = [['L1','Lab 1'],['L2','Lab 2'],['L3','Lab 3']])
	
	date = forms.DateField(widget = forms.widgets.SelectDateWidget())