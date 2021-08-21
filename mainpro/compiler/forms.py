from django import forms
from .models import GetInfor

class GetInforforms(forms.ModelForm):
	class Meta:
		model = GetInfor
		fields = ['namefile', 'pathfile', 'parameter']
