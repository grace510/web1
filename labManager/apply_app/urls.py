from django.urls import path
from . import views

urlpatterns = [
    path('showExps/', views.showExperiments,name="applyshowExps"),
    path('showExps/selectExperiment/',views.selectExperiment,name="apply"),
    path('showExps/selectExperiment/createApplicant',views.createApplicant),
]