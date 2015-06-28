from django import forms 

class Problema(forms.Form):
	titulo_problema = forms.CharField(max_length=320)
	planteamiento   = forms.CharField() 