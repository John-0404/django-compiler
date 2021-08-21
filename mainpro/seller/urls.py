from django.urls import path
from .import views

app_name = 'seller'

urlpatterns = [
    path('sellerx1/', views.seller1,name = "sellerx1"),
    path('save/', views.saveSeller, name = "saveSeller1"),
    path('output/', views.output ,name = "list"),
    path('<int:id>/', views.detail, name= "detaillist"),
   

]
