from django.shortcuts import render
from django.template import loader
from .models import Newssource

# Create your views here.
from django.http import HttpResponse, Http404

from .sentiment_extractor import SentimentExtractor
from .keyword_retriever import KeywordRetriever
from .headline_retriever import HeadlineRetriever

def chart_display(request):
	sent_extractor = SentimentExtractor()
	info = sent_extractor.get_all_news_sources()

	mylabels = info[0]
	mydata = info[1]
	vader_data = sent_extractor.get_all_news_source_vader_values()

	context = {'my_perc_labels':mylabels, 
			   'my_perc_data':mydata,
			   'my_hist_data':vader_data}

	return render(request, 'headlines/chart_display.html', context)

def chart_neg_pos(request):
	sent_extractor = SentimentExtractor()

	vader_data = sent_extractor.get_all_news_source_vader_values()
	return render(request, 'headlines/chart_neg_pos.html', {'my_hist_data':vader_data})

def keyword_cloud(request):
	keyword_retriever = KeywordRetriever()
	info = keyword_retriever.keyword_frequencies(limit = 150)
	return render(request, 'headlines/keyword_cloud.html', {'mydata':info})

def headline_display(request, word):
	try:
		hr = HeadlineRetriever()
		headlines = hr.get_headlines()
		news_sources = ["abc", "nbc", "fox", "reuters"]
		months = ['January', 'February', 'March', 'April', 'May', 'June', 
				  'July', 'August', 'September', 'October', 'November', 'December']
		days = list(range(1, 32))

	except:
		raise Http404("Keyword does not exist!")
	
	context = {'kw': word, 
				'headlines': headlines, 
				'newssources': news_sources,
				'months': months,
				'days': days}
	return render(request, 'headlines/display_headlines.html', context)

def keyword_display(request):
	kr = KeywordRetriever()
	info = kr.keyword_frequencies()
	context = {"kws": info}

	return render(request, 'headlines/keyword_list.html', context)

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
