from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import date


lab_choices = (

		('L1','Lab 1'),
		('L2','Lab 2'),
		('L3','Lab 3'),

	)



class SurfaceWaterData(models.Model):
	dissolved_oxygen = models.FloatField()  				 
	ph_val = models.FloatField(
		validators = [MaxValueValidator(14),MinValueValidator(0)]
			)
	electrical_conductivity = models.FloatField()
	total_dissolved_solids = models.FloatField()
	total_alkalinity = models.FloatField()
	total_hardness = models.FloatField()
	total_suspended_solids = models.FloatField()
	calcium = models.FloatField()
	magnesium = models.FloatField()
	chlorides = models.FloatField()
	nitrate = models.FloatField()
	sulphate = models.FloatField()
	biological_oxygen_demand = models.FloatField()
	quality_index = models.FloatField()

	#data not related to quality
	water_body_name = models.CharField(max_length = 140)
	lat = models.FloatField()
	lon = models.FloatField()
	user = models.ManyToManyField(User)
	
	date = models.DateField(default = date.today)
	


class SurfaceWaterDataTemp(models.Model):
	dissolved_oxygen = models.FloatField()  				 
	ph_val = models.FloatField(
		validators = [MaxValueValidator(14),MinValueValidator(0)]
			)
	electrical_conductivity = models.FloatField()
	total_dissolved_solids = models.FloatField()
	total_alkalinity = models.FloatField()
	total_hardness = models.FloatField()
	total_suspended_solids = models.FloatField()
	calcium = models.FloatField()
	magnesium = models.FloatField()
	chlorides = models.FloatField()
	nitrate = models.FloatField()
	sulphate = models.FloatField()
	biological_oxygen_demand = models.FloatField()
	quality_index = models.FloatField()

	#data not related to quality
	water_body_name = models.CharField(max_length = 140)
	lat = models.FloatField()
	lon = models.FloatField()
	user = models.ManyToManyField(User)
	
	date = models.DateField(default = date.today)



class WaterData(models.Model):
	dissolved_oxygen = models.FloatField()  				 
	ph_val = models.FloatField(
		validators = [MaxValueValidator(14),MinValueValidator(0)]
			)
	electrical_conductivity = models.FloatField(null = True)
	total_dissolved_solids = models.FloatField(null = True)
	total_alkalinity = models.FloatField(null = True)
	total_hardness = models.FloatField(null = True)
	total_suspended_solids = models.FloatField(null = True)
	calcium = models.FloatField(null = True)
	magnesium = models.FloatField(null = True)
	chlorides = models.FloatField(null = True)
	nitrate = models.FloatField(null = True)
	sulphate = models.FloatField(null = True)
	biological_oxygen_demand = models.FloatField(null = True)
	quality_index = models.FloatField(null = True)
	temperature = models.FloatField()
	colour = models.CharField(max_length = 25)
	odour = models.IntegerField(null = True)
	chemical_oxygen_demand = models.FloatField(null = True)
	iron = models.FloatField(null = True)
	potassium = models.FloatField(null = True)
	phosphate = models.FloatField(null = True)
	nitrate = models.FloatField(null = True)
	nitrite = models.FloatField(null = True)
	boron = models.FloatField(null = True)
	bicarbonate = models.FloatField(null = True)
	fluoride = models.FloatField(null = True)
	total_plate_count  = models.FloatField(null = True)
	total_coliform = models.FloatField(null = True)
	fecal_coliform = models.FloatField(null = True)
	e_coliform = models.FloatField(null = True)
	sodium = models.FloatField(null = True)
	carbonate = models.FloatField(null = True)
	silicate = models.FloatField(null = True)
	total_organic_carbon = models.FloatField(null = True)
	total_kjelhdal_nitrogen = models.FloatField(null = True)
	ammonia_nitrogen = models.FloatField(null = True)
	cyanide = models.FloatField(null = True)
	arsenic = models.FloatField(null = True)
	cadium = models.FloatField(null = True)
	mercury = models.FloatField(null = True)
	chromium = models.FloatField(null = True)
	lead  = models.FloatField(null = True)
	zinc = models.FloatField(null = True)


	#meta data about water body 
	water_body_name = models.CharField(max_length = 140,default = 'Ganga')
	lat = models.FloatField(default = 78.123445)
	lon = models.FloatField(default = 78.123445)
	user = models.ManyToManyField(User)
	laboratory = models.CharField(max_length= 5,choices = lab_choices,default = 'L1')
	
	date = models.DateField(default = date.today)



class WaterDataTemp(models.Model):
	dissolved_oxygen = models.FloatField()  				 
	ph_val = models.FloatField(
		validators = [MaxValueValidator(14),MinValueValidator(0)]
			)
	electrical_conductivity = models.FloatField(null = True)
	total_dissolved_solids = models.FloatField(null = True)
	total_alkalinity = models.FloatField(null = True)
	total_hardness = models.FloatField(null = True)
	total_suspended_solids = models.FloatField(null = True)
	calcium = models.FloatField(null = True)
	magnesium = models.FloatField(null = True)
	chlorides = models.FloatField(null = True)
	nitrate = models.FloatField(null = True)
	sulphate = models.FloatField(null = True)
	biological_oxygen_demand = models.FloatField(null = True)
	quality_index = models.FloatField(null = True)
	temperature = models.FloatField(null = True)
	colour = models.CharField(max_length = 25)
	odour = models.IntegerField(null = True)
	chemical_oxygen_demand = models.FloatField(null = True)
	iron = models.FloatField(null = True)
	potassium = models.FloatField(null = True)
	phosphate = models.FloatField(null = True)
	nitrate = models.FloatField(null = True)
	nitrite = models.FloatField(null = True)
	boron = models.FloatField(null = True)
	bicarbonate = models.FloatField(null = True)
	fluoride = models.FloatField(null = True)
	total_plate_count  = models.FloatField(null = True)
	total_coliform = models.FloatField(null = True)
	fecal_coliform = models.FloatField(null = True)
	e_coliform = models.FloatField(null = True)
	sodium = models.FloatField(null = True)
	carbonate = models.FloatField(null = True)
	silicate = models.FloatField(null = True)
	total_organic_carbon = models.FloatField(null = True)
	total_kjelhdal_nitrogen = models.FloatField(null = True)
	ammonia_nitrogen = models.FloatField(null = True)
	cyanide = models.FloatField(null = True)
	arsenic = models.FloatField(null = True)
	cadium = models.FloatField(null = True)
	mercury = models.FloatField(null = True)
	chromium = models.FloatField(null = True)
	lead  = models.FloatField(null = True)
	zinc = models.FloatField(null = True)


	#meta data about water body 
	water_body_name = models.CharField(max_length = 140,default = 'Ganga')
	lat = models.FloatField(default = 78.123445)
	lon = models.FloatField(default = 78.123445)
	user = models.ManyToManyField(User)
	laboratory = models.CharField(max_length = 5,choices = lab_choices,default = 'L1')
	flag = models.CharField(max_length = 1,choices = (('1','1'),('0','0')))
	date = models.DateField(default = date.today)


# class Approve(models.Model):
# 	user = models.ForeignKey(User,on_delete = models.CASCADE)
# 	data = models.ForeignKey(WaterData,on_delete = models.CASCADE)

# class Reject(models.Model):
	
# 	reason = models.CharField(max_length = 25000)
# 	data = models.ForeignKey(WaterData,on_delete = models.CASCADE)