from django.shortcuts import render
from django.template import loader
from .models import Newssource

# Create your views here.
from django.http import HttpResponse, Http404

from .sentiment_extractor import SentimentExtractor
from .keyword_retriever import KeywordRetriever

def chart_neg_pos(request):
	sent_extractor = SentimentExtractor()
	info = sent_extractor.get_all_news_sources()

	mylabels = info[0]
	mydata = info[1]
	
	return render(request, 'headlines/chart_neg_pos.html', {'mylabels':mylabels, 'mydata':mydata})

def keyword_cloud(request):
	keyword_retriever = KeywordRetriever()
	info = keyword_retriever.keyword_frequencies()

	return render(request, 'headlines/keyword_cloud.html', {'mydata':info})

def headline_display(request, word):
	try:
		keyword_retriever = KeywordRetriever()
		inp = None if word=="ALL" else word
		headlines = keyword_retriever.get_headlines(kw = inp)
		keywords = keyword_retriever.get_keywords()
	except:
		raise Http404("Keyword does not exist!")
	
	context = {'kw': word, 'headlines':headlines, 'kws': keywords}
	return render(request, 'headlines/display_headlines.html', context)


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
