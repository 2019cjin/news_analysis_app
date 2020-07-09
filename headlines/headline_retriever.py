from .models import Headline, Keyword, Headlinekeyword, Newssource

class HeadlineRetriever(object):
	"""docstring for HeadlineRetriever"""
	def __init__(self):
		"""Initializes querysets for keyword and headlinekeyword"""
		self.keyword_queryset = Keyword.objects.all()
		self.headlinekeyword_queryset = Headlinekeyword.objects.all()
		self.headline_queryset = Headline.objects.all()

	def get_unique_headline(self, queryset):
		"""Returns a list of unique headlines"""
	def get_headlines(self):
		"""Returns a list with headline"""
		seen_headlines = set()
		new_headlines  = []
		for headline in self.headline_queryset:
			if headline.content not in seen_headlines:
				seen_headlines.add(headline.content)
				new_headlines.append(headline)
		return new_headlines

	def get_headlines_with_keyword(self, word):
		"""Returns a queryset with headline containing the keyword"""
		pass