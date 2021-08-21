from django import forms

class seller_Forms(forms.Form):
	name = forms.CharField(max_length = 25)
	product = forms.CharField(widget = forms.Textarea)