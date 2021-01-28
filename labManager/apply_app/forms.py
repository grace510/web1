from django.forms import ModelForm
from .models import Applicant

class TodoForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ['id','name','desc','phoneNum','date','expID',]