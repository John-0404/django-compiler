from django.urls import path
from . import views
app_name = 'compiler'
urlpatterns	=	[
	path('getinfor/', views.GetInfor, name = "getinfor"),
	path('output/', views.submitInfor, name = "submit"),
	path('process/', views.process, name = "process"),
	
	]