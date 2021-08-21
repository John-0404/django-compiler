from django.urls import path
from .import views

app_name = 'loghome'

urlpatterns = [
    path('1/', views.index1),
    path('2/', views.index2),
    path('3/', views.index3, name = 'loghome'),
    path('4/', views.post1, name = 'post1'),
    path('', views.homep, name = 'homep'),
    

]
