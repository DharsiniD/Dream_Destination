
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="homepage"),
    path('test/',views.samp),
    path('login1',views.login,name="loginpage"),
    path('register1',views.register,name="registerpage"),
    path('logout',views.logout),
   
    
    ]
