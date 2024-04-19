from django.urls import path
from app2 import views
from app3 import views
urlpatterns = [
   # path("addemp",views.addemp,name='addemp'),
   path("add/",views.details,name='add'),
   
   
]