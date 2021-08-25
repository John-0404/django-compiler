from django.shortcuts import render
from django.http import HttpResponse
import os
import subprocess
from .models import GetModel
from .forms import GetForms

# Create your views here.

def GetInfor(request):
	Gf = GetForms
	return render(request, 'export2lna/input.html',{'Gf' : Gf})

def submitInfor(request):
	form = GetForms(request.POST)
	if form.is_valid():
		name1 = form.cleaned_data['name']
		path1 = form.cleaned_data['path']
		para1 = form.cleaned_data['para']
		out1 = process(name1,path1,para1)
		form.instance.out = out1
		form.save()
		return render(request, 'export2lna/output.html',{'out1' :out1})
	else:
		return HttpResponse('false')

def process(name,path,para):
	command = "g++ -o "+ name +" "+ name + ".cpp"
	subprocess.run(command,cwd=path)
	result = subprocess.run(para,
							cwd= path,
	                        shell=True, 
	                        stdout = subprocess.PIPE,
	                        stderr = subprocess.PIPE)
	print("-------------------------------")	
	Rs = result.stdout.decode("utf-8")
	return Rs
	#return render(request, 'compiler/output.html', {'Rs' : Rs})
