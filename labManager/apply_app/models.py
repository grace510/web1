from django.db import models

# Create your models here.

#[id, name, phoneNum, desc]

class Applicant(models.Model): #임포트한 models로부터 Model 상속
    objects = models.Manager()
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    phoneNum = models.IntegerField(null=True)
    expID = models.IntegerField(null=True)
    date = models.DateField(null=True)
    isConfirmed = models.BooleanField(default=False)