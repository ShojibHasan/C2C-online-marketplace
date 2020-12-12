from django.urls import path,include

from index import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:category_id>',views.category,name='category'),
    path('post_ads/',views.post_ads,name='post_ads'),
]