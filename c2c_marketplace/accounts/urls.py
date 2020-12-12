from django.urls import path
from . import views
# from accounts import views


urlpatterns =[
    path('register/',views.register,name ='register'),
    path('login/',views.login,name ='login'),
    path('logout/',views.userlogut,name ='logout'),
    path('dashboard/',views.dashboard,name ='dashboard'),
]