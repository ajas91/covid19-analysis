from django.urls import re_path
from analysisUI import views

urlpatterns = [
    re_path('^$',views.indexPage,name='index'),
    re_path('',views.indivitualCountryData,name='countries')
]