from django.urls import path
from . import views
app_name = 'contact'
urlpatterns	=	[
path('contactp/',views.contact, name =	'contactp'),
path('getcontact/',views.getContact, name = "getContact"),
path('listcontact/', views.listContact, name = "listcontact"),
path('<int:id>/',views.detailContact, name = "detailcontact"),
	]