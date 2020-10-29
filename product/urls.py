from django.urls import path
from . import views

urlpatterns = [
    path('',views.productlist,name='product_list'),
    path('<id:int>',views.productdetail,name='product_detials'),
]