from django import forms
from .models import UploadForm

class UploadFileForm(forms.ModelForm):
	class Meta:
		model = UploadForm
		fields = ['title', 'file', 'body']
