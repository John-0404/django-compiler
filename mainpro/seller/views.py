from django.shortcuts import render
from django.http import HttpResponse
from .forms import seller_Forms
from .models import sellerForm

# Create your views here.
def seller1(request):
	cf = seller_Forms	
	return render(request,'seller/indexsell.html',{ 'cf': cf })
def saveSeller(request):
	if	request.method == "POST":
		cf = seller_Forms(request.POST)
		if cf.is_valid():
			saveCf = sellerForm(name = cf.cleaned_data['name'],
					product = cf.cleaned_data['product'],)
			saveCf.save()
			return HttpResponse('save success')
	else:
		return HttpResponse(' false')

def output(request):
	Out = sellerForm.objects.all()
	return render(request,'seller/listseller.html', {'Out':Out})


def detail(request, id):
	Opd = sellerForm.objects.get(id = id)
	return render(request, 'seller/detail.html', {'Opd':Opd})
