from django.shortcuts import render
from apply_app.models import Applicant
from django.http import HttpResponse
from .models import Experiment
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count


#홈 대시보드
def showExperiments(request):
    exps = Experiment.objects.all().values()
    applicants = Applicant.objects.all().filter(isConfirmed=True).values()
    waitings = Applicant.objects.all().filter(isConfirmed=False).values()

    for app in applicants:
        for exp in exps:
            if exp['id']==app['expID']:
                app['expName'] = exp['name']


    context = {"exps":exps,"applicants":applicants,"waitings":waitings}
    return render(request,'admin_app/listExps.html',context)      


#실험추가 폼 생성
def showExpForm(request):
    return render(request,'admin_app/createExpForm.html')


#실험추가 폼 제출
def createExperiment(request):
    name = request.POST['name']
    desc = request.POST['desc']
    targetNum = request.POST['targetNum']
    newExp = Experiment(name=name, desc=desc,targetNum=targetNum)
    newExp.save()
    return HttpResponseRedirect(reverse('showExps'))


#피험자 컨펌 폼 생성
def showConfirmForm(request):
    applicant_id = request.GET.get('Aid')
    exp_id = request.GET.get('Eid')
    applicants = Applicant.objects.all().filter(expID=exp_id)
    exp = Experiment.objects.get(id=exp_id)
    context = {"applicants":applicants,"expName":exp.name,"expID":exp_id,"applicant_id":applicant_id}
    return render(request,'admin_app/confirmApplicant.html',context)


#피험자 컨펌 폼 제출
def confirmApplicant(request):
    applicant_id = request.POST.get('Aid','')
    exp_id = request.POST.get('Eid','')
    applicants = Applicant.objects.all().filter(expID=exp_id)
    exp = Experiment.objects.get(id=exp_id)
    context = {"applicants":applicants,"expName":exp.name,"expID":exp_id}
    date = request.POST.get('date','')
    
    applicant = Applicant.objects.get(id=applicant_id)
    applicant.isConfirmed=True
    applicant.date = date
    applicant.save()
    #return render(request,'admin_app/listApplicants.html',context)
    return HttpResponseRedirect(reverse("showApplicants"))  


#실험별 피험자 목록
def selectExperiment(request):
    exp_id = request.GET.get('id')
    print(exp_id)
    applicants = Applicant.objects.all().filter(expID=exp_id,isConfirmed=False)
    exp = Experiment.objects.get(id=exp_id)
    context = {"applicants":applicants,"expName":exp.name,"expID":exp_id} #html에서 {{expID}}로 호출함
    return render(request,'admin_app/listApplicants.html',context)


#피험자 데이터 삭제
def deleteApplicant(request):
    delete_applicant_id = request.GET.get('Aid')
    exp_id = request.GET['Eid']
    applicants = Applicant.objects.all().filter(expID=exp_id)
    exp = Experiment.objects.get(id=exp_id)
    context = {"applicants":applicants,"expName":exp.name,"expID":exp_id}

    applicant = Applicant.objects.get(id=delete_applicant_id)
    applicant.delete()
    #return HttpResponseRedirect(reverse("showApplicants"))
    return render(request,'admin_app/listApplicants.html',context)


#테스트용 - DB의 모든 피험자 데이터 불러오기
def showApplicants(request):
    applicants = Applicant.objects.all()
    context = {"applicants":applicants}
    return render(request,'admin_app/listApplicants.html',context)