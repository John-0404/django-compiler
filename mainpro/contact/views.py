from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_Form
from .models import contactForm
import subprocess
import os

# Create your views here.

def contact(request):
	cf = contact_Form
	return render(request,'contact/contact.html',{'cf':cf})

# cach 1 la dung ham get de luu thong tin va check thong
def getContact(request):
	if request.method == "POST":
		cf = contact_Form(request.POST)
		print("-------------------")

		#af = cf.username
		#print(af)
		
		#form.instance.out = processcpp(form.instance.)

		print("-------------------")
		if cf.is_valid():
			
			print(cf.cleaned_data['username'])
			cf.save()
			return HttpResponse("save success")
	else:
		return HttpResponse("not POS  T") 

def listContact(request):
	lc = contactForm.objects.all()
	return render(request, 'contact/listcontact.html', {'lc':lc})

def detailContact(request, id):
	dt = contactForm.objects.get(id = id)
	return render(request, 'contact/detailContact.html', {'dt': dt})


def processcpp(name,path,para):
	name = "name.exe"
	command = "g++ -o "+ name +" "+ name + ".cpp"
	path = "C:\\Users\\Admin\\Desktop\\lab\\learn_python\\calltool"
	para = "dinh bao thien la 5 va 10"
	
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
	
	#print(Rs)
	#print (path)
	#return render(request, 'compiler/output.html', {'Rs' : Rs})
