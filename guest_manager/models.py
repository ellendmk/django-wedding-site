from django.db import models
import uuid

# Create your models here.
class guests(models.Model):
    # p_id = models.IntegerField(default=0,primary_key = True)
    name = models.CharField(max_length=200)
    child = models.BooleanField()
    family_id = models.IntegerField()
    email = models.EmailField(max_length=200)
    responded = models.BooleanField(null=True, blank=True)
    attending = models.BooleanField(null=True, blank=True)
    fun = models.BooleanField()
    # diet = models.CharField(max_length=200,blank=True,null=True)
    message = models.CharField(max_length=1000,blank=True,null=True)

class families(models.Model):
	family_id = models.IntegerField()
	url_suffix = models.CharField(max_length=200)
	child_allowed = models.BooleanField(null=True, blank=True)