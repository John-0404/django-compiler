from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from .models import GetInfor
from .forms import GetInforforms
import os
# Create your views here.

def GetInfor(request):
	Gf = GetInforforms
	return render(request, 'compiler/compiler.html', {'Gf' : Gf})

def submitInfor(request):
	form = GetInforforms(request.POST)
	if form.is_valid():
		name1 = form.cleaned_data['namefile']
		path1 = form.cleaned_data['pathfile']
		para1 = form.cleaned_data['parameter']
		out = process(name1,path1,para1)
		form.instance.Res = out
		print(out)

		form.save()
		return HttpResponse('success')
	else:
		return HttpResponse("not POS  T") 

def process(name,path,para):
	# vđ cần truyền tham số, path, tên file
	#Op = GetInfor.objects.all()
	#path = Op.pathFile

	# ý là muốn truyền dữ liệu của field pathfile cho biến là path
	#path = GetInfor.pathfile

	#command = "g++ -o name name.cpp"
	#path = "C:\\Users\\Admin\\Desktop\\lab\\learn_python\\calltool"
	#para = "dinh bao thien la 5 va 10"
	#data, temp = os.pipe()
	#name = "name.exe"
	command = "g++ -o "+ name +" "+ name + ".cpp"
	#path = "C:\\Users\\Admin\\Desktop\\lab\\learn_python\\calltool"
	#para = "dinh bao thien la 5 va 10"
	
	data, temp = os.pipe()
	os.write(temp, bytes(para, "cp932"));
	os.close(temp)
	subprocess.run(command,cwd=path)
	result = subprocess.run(name,
							cwd= path,
	                        shell=True, 
	                        stdin = data,
	                        stdout = subprocess.PIPE,
	                        stderr = subprocess.PIPE)
	print("-------------------------------")
	file = open(r"C:\Users\Admin\Desktop\lab\filetext.txt", "w")
	file.write( str(result.stdout.decode("cp932")) )
	file.close()
	Rs = result.stdout.decode("cp932")	
	return Rs
	#return render(request, 'compiler/output.html', {'Rs' : Rs})
