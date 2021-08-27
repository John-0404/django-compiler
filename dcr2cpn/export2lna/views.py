from django.shortcuts import render
from django.http import HttpResponse
import os
import subprocess
from .models import GetModel
from .forms import GetForms
import textract
from pathlib import Path

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
		form.instance.out = process(name1,path1,para1)
		a = process(name1,path1,para1)
		form.save()
		return render(request, 'export2lna/output.html', {'a' : a})
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
	old = r'C:\\Users\\Admin\\Desktop\\lab\\learn_python\\django\\SmartContractChecking-Application\\tools\\dcr2cpn\\test.lna'
	new = r'C:\\Users\\Admin\\Desktop\\lab\\learn_python\\django\\SmartContractChecking-Application\\tools\\dcr2cpn\\test.txt'
	os.rename(old, new)
	text = textract.process(r'C:\\Users\\Admin\\Desktop\\lab\\learn_python\\django\\SmartContractChecking-Application\\tools\\dcr2cpn\\test.txt')
	text = text.decode("utf-8")
	file = open(r"C:\Users\Admin\Desktop\filetext.lna", "w")
	file.write( text )
	return text
	