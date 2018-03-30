from django.shortcuts import render,redirect

from django.utils import timezone
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from login.forms import LoginForm,RegistrationForm
from login.models import OrganizationDetails
# Create your views here.

def index(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
			# if users:
			# 	print(user.users)
			try:
				login(request,user)
				return redirect('/')

			except:
				return render(request,'login/index.html',{"error":"Username or password incorrect"})
		return render(request,'login/index.html',{"error":"Form not Valid"})
	return render(request,'login/index.html')


def logout_user(request):
	logout(request)
	return redirect('/')


def register(request):
	if request.method == 'POST':
		regForm = RegistrationForm(request.POST)
		if regForm.is_valid():
			try:
				username = regForm.cleaned_data['email']
				email = username
				first_name = regForm.cleaned_data['first_name']
				last_name = regForm.cleaned_data['last_name']
				org_name = regForm.cleaned_data['org_name']
				org_id = regForm.cleaned_data['org_id']
				password = regForm.cleaned_data['password']
				user = User.objects.create_user(username = username,password = password)
				user.first_name = first_name
				user.last_name = last_name
				user.email = email
				#user.users = 'organisation'
				#user.set_password = password
				
				org_det = OrganizationDetails()
				org_det.org_name = org_name
				org_det.org_id = org_id
				org_det.user = user
				group = Group.objects.get(name='gov_official')
				if "@gov.in" not in email:
					group = Group.objects.get(name='private_organization')
				
				user.save()
				user.groups.add(group)
				org_det.save()
				login(request,user)	
				return redirect('/')
				
			except:
				return render(request,'login/register.html',{"error_message":"Organization or email already exists!"})
			
				
	return render(request,'login/register.html')


