from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Newssource

def index(request):
	template = loader.get_template('headlines/home.html')
	context = {}
	return HttpResponse(template.render(context, request))

def news_websites(request):
    news_list = Newssource.objects.all()
    template = loader.get_template('headlines/news_websites.html')
    context = {
        'news_list': news_list,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('headlines/about.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def process(request):
    news_list = Newssource.objects.all()
    template = loader.get_template('headlines/process.html')
    context = {
        'news_list': news_list,
    }
    return HttpResponse(template.render(context, request))