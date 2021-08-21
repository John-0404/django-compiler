from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from .models import UploadForm
from .forms import UploadFileForm

# Create your views here.

#def open(request):
#	subprocess.call('C://Users//Admin//Desktop//ToolCovertToJson//ToolConvertToJson.exe')

def UploadFile(request):
	subprocess.call('C://Users//Admin//Desktop//ToolCovertToJson//ToolConvertToJson.exe')
	Uf = UploadFileForm
	return render(request, 'callTool/upload.html', {'Uf' : Uf} )

def getFile(request):
	form = UploadFileForm(request.POST, request.FILES)
	if form.is_valid():
		form.save()
	return HttpResponse("save success")

def openTool(request):
	subprocess.call('C://Users//Admin//Desktop//ToolCovertToJson//ToolConvertToJson.exe')

def listfile(request):
	lf = UploadForm.objects.all()
	return render(request, 'callTool/listfile.html', {'lf':lf})

def detailfile(request, id):
	dt = UploadForm.objects.get(id=id)
	return render(request, 'callTool/detailfile.html', {'dt':dt})

