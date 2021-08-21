from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import(
    ToolCreateView,
    ToolDetailView,
)
from . import views

urlpatterns = [
    path('', views.about, name='tool-about'),
    path('tool/', ToolCreateView.as_view(), name='tool-create'),
    path('tool/<int:pk>/', ToolDetailView.as_view(), name='tool-detail'),
]