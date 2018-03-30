from django import forms



class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget = forms.PasswordInput())


class RegistrationForm(forms.Form):
	email = forms.EmailField()
	first_name = forms.CharField(max_length = 140)
	last_name = forms.CharField(max_length = 140)
	password = forms.CharField(widget = forms.PasswordInput())
	org_name = forms.CharField(max_length = 140)
	org_id = forms.IntegerField()

