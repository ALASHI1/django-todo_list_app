from django.db import models

# Create your models here.

class TdList(models.Model):
    title = models.CharField(max_length=250)
    def __str__(self): 
	    return self.title