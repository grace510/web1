from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from admin_app.models import Experiment
from .models import Applicant
from django.urls import reverse
from flask import Flask,render_template
from django.utils import timezone

#실험목록 디스플레이
def showExperiments(request):
    exps = Experiment.objects.all()
    context = {"exps":exps}
    return render(request,'apply_app/list.html',context)
    
    
#선택한 실험을 신청하는 페이지 디스플레이
def selectExperiment(request):
    exp_id = request.GET.get('id')
    exp_name = request.GET.get('name')
    print(exp_id)
    print(exp_name)
    context = {"expID":exp_id,"expName":exp_name} 
    return render(request,'apply_app/application.html',context)
    

#신청폼 제출 - Applicant 객체 생성되어 DB에 저장
def createApplicant(request):   
    name = request.POST['name']
    phoneNum = request.POST['phoneNum']
    desc = request.POST['desc']
    expID = request.POST['expID']
    date = timezone.now()

    print(name)
    print(phoneNum)
    print(desc)
    print(expID)
    new_applicant = Applicant(name=name,phoneNum=phoneNum,desc=desc,expID=expID,date=date)
    new_applicant.save()

    return HttpResponseRedirect(reverse('applyshowExps'))

