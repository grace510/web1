from django.urls import path
from . import views

urlpatterns = [
    path('showExps/', views.showExperiments,name="showExps"),
    path('showExps/selectExperiment/',views.selectExperiment,name="showApplicants"),
    path('showExps/ExpForm/',views.showExpForm,name="ExpForm"),
    path('showExps/ExpForm/createExperiment',views.createExperiment),
    path('showExps/selectExperiment/deleteApplicant/',views.deleteApplicant),  
    path('showExps/selectExperiment/showConfirmForm/confirmApplicant/',views.confirmApplicant),
    path('showExps/selectExperiment/showConfirmForm/',views.showConfirmForm),
    path('showExps/createExperiment/', views.createExperiment),

]