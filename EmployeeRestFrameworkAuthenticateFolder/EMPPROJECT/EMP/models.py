from django.db import models

class EmpModel(models.Model):
    empnm = models.CharField(max_length=35)
    empadd = models.CharField(max_length=35)
    empsal = models.FloatField()
