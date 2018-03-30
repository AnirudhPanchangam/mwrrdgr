from django.db import models
from django.contrib.auth.models import User

class OrganizationDetails(models.Model):
	org_name = models.CharField(max_length = 140)
	org_id = models.IntegerField(unique=True)
	user = models.ForeignKey(User,on_delete = models.CASCADE)

