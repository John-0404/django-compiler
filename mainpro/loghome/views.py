from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index1(request):
	return HttpResponse('day la bai tap 1')
def index2(request):
	return	HttpResponse('day la bai tap 2')	
def index3(request):
	return render(request,'loghome/index.html')
def post1(request):
	return render(request,'loghome/post1.html')
def homep(request):
	return render(request,'loghome/homep.html')