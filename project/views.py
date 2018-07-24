from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from .models import Records
from .forms.create_form import AddForm

def index(request):
    return render_to_response('index.html')

def list(request):
    records = Records.objects.all()
    context = {"records" : records}
    return render(request, 'list.html', context)

def add(request):
	form = AddForm()
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():
			new_record = form.save()
			return HttpResponseRedirect('list')

	context = {"form" : form}
	return render(request, 'add.html', context)