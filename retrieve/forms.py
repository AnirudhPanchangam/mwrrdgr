from django import forms
from input.models import SurfaceWaterData
from itertools import chain
from retrieve.attr import retAttr
ob = SurfaceWaterData.objects.all().order_by('water_body_name','date')
water_name = []
year = []
for i in range(0,len(ob)):
	if str(ob[i].date.year) in chain(*year):
		pass
	else:
		year.append([str(ob[i].date.year),str(ob[i].date.year)])
		

for i in range(0,len(ob)):
	if ob[i].water_body_name in chain(*water_name):
		pass
	else:
		water_name.append([str(ob[i].water_body_name),str(ob[i].water_body_name)])
		

tuple(water_name)
class ListOfParams(forms.Form):
	name_of_river = forms.ChoiceField(choices=water_name)
	year = forms.ChoiceField(choices=year)

class ListOfAttr(forms.Form):
	name_of_river = forms.ChoiceField(choices = water_name)
	parameters = forms.MultipleChoiceField(choices = retAttr() )

class FormForPdf(forms.Form):
	name_of_river = forms.ChoiceField(choices=water_name)
	year_beg = forms.ChoiceField(choices=year)
	year_end = forms.ChoiceField(choices=year)
