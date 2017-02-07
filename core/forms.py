from django import forms


class FormContact(forms.Form):
	""" Gera o formulario de contato"""
	
	name = forms.CharField(label='Nome', widget=forms.TextInput())
	email = forms.EmailField(label='Email', widget=forms.TextInput())
	phone = forms.CharField(label='Telefone', max_length=13, widget=forms.TextInput())
	message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), max_length=500 )