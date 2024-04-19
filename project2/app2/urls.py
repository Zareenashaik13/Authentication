from django.urls import path
from app2 import views

urlpatterns = [
    path('display/<int:emp_id>',views.display,name = "disp"),
    path("signin/",views.signin,name='signin'),
    path("login/",views.handlelogin,name="login"),
]
