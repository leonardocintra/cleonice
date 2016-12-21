import os
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.views.generic import TemplateView

from .forms import FormContact
from .models import IndexMediaCarrousel, IndexMediaCircle, IndexMediaPhotoFeatured


def index(request):
	carrousels = IndexMediaCarrousel.objects.all()
	circles = IndexMediaCircle.objects.all()
	photosFeature = IndexMediaPhotoFeatured.objects.all()

	context = {
		'carrousels':carrousels,
		'circles': circles,
		'photosFeature': photosFeature,
	}

	return render(request, 'index.html', context)

def contact(request):
	title = "Contato"
	if request.method == "POST":
		form = FormContact(request.POST)
		if form.is_valid():
			recipient = [os.environ['EMAIL_HOST_USER']]
			sender = form.cleaned_data['email']
			subject = "CONTATO - " + form.cleaned_data['name']
			message = " TELEFONE: " + form.cleaned_data['phone'] + "\n MENSAGEM:" + form.cleaned_data['message'] + "\n EMAIL: " + form.cleaned_data['email']
			print("Contact: email sent to: " + sender)
			send_mail(subject, message, sender, recipient)
			return render(request, 'contato.html', {'form': FormContact(), 'send': True, 'title': title })
	else:
		form = FormContact()			

	return render(request, 'contato.html', {'title': title, 'form':form })


class AboutView(TemplateView):
	template_name = 'sobre.html'


about = AboutView.as_view()