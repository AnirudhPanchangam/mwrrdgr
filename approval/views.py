from django.shortcuts import render
from input.models import WaterDataTemp,WaterData
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
		data_final = WaterData()
	return render(request,'approval/approved.html',{})