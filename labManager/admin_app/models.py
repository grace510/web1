from django.db import models
# Create your models here.
# entity
# sqlite에서 테이블관리

#__init__ 없이 사용하는 것이 스펙문서 가이드
#생성자 세팅 없어도 부모인 Model에 의해 다 처리됨
#[ID, name,desc]
class Experiment(models.Model): #임포트한 models로부터 Model 상속
   objects = models.Manager()
   name = models.CharField(max_length=255)
   desc = models.CharField(max_length=255)
   targetNum = models.IntegerField(default=40)
   isConfirmed = models.BooleanField(default=False)
