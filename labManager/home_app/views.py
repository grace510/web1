from django.shortcuts import render

# Create your views here.

def directUserPage(request):
    return render(request,'home_app/index.html')
    #get userType
    userType = 0#admin
    userType = 1#applicant
    
    #direst to user page 
    if(userType== 0):
        return render(request,'/admin_app/listExps.html')
    elif(userType== 1):
        return render(request,'/admin_app/listExps.html')