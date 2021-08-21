from django.urls import path
from .import views

app_name = 'callTool'

urlpatterns	=	[
	path('upload/', views.UploadFile, name= "upfile"),
    path('getfile/',views.getFile, name = "getfile"),
	path('op/', views.openTool, name = "opentool"),
	path('listfile/', views.listfile, name = "listfile"),
	path('<int:id>/',views.detailfile, name = "detailfile"),
	]