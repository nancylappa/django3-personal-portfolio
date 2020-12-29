from django.urls import path, include
from . import views

app_name = 'blog' #to xrisimopoioume sto detail.html se periptosi poy yparxei to detail kai se alla apps

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:post_id>/', views.detail, name='detail'), #pernav parametro to id tou post

]