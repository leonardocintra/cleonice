from django import forms


class FormContact(forms.Form):
	name = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
	phone = forms.CharField(label='Telefone', max_length=13, widget=forms.TextInput(attrs={'class': 'form-control'}))
	message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=500 )