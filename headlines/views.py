from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Headline, Headlinekeyword, Keyword, Newssource
from .sentiment_extractor import SentimentExtractor

def index(request):
	return HttpResponse("Hello, world. You're at the headlines index.")
def chart_neg_pos(request):
	sent_extractor = SentimentExtractor()
	info = sent_extractor.get_all_news_sources()

	mylabels = info[0]
	mydata = info[1]
	
	return render(request, 'headlines/chart_neg_pos.html', {'mylabels':mylabels, 'mydata':mydata})