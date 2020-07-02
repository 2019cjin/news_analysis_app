from .models import Headline, Keyword, Headlinekeyword, Newssource


class KeywordRetriever(object):
	"""docstring for KeywordRetriever"""
	def __init__(self):
		"""Initializes querysets for keyword and headlinekeyword"""
		self.keyword_queryset = Keyword.objects.all()
		self.headlinekeyword_queryset = Headlinekeyword.objects.all()
		self.headline_queryset = Headline.objects.all()

	def keyword_headlines(self):
		"""Returns a dictionary of the keywords and the list of corresponding headlines (ids only)"""
		d = {}

		for q in self.keyword_queryset:
			d[q.content] = self.headlinekeyword_queryset.filter(keywordid = q.id)

		return d

	def get_keywords(self):
		"""Returns a list of keywords"""
		return list(self.keyword_headlines().keys())
		
	def keyword_frequencies(self):
		"""Returns a list of lists [word, number of headlines]"""
		key_head = self.keyword_headlines()

		freq_list = []
		for keyword in key_head:
			freq_list.append([keyword, len(key_head[keyword])])

		return freq_list

	def get_headlines_with_keyword(self, kw):
		"""Returns a list of the headlines with the corresponding keyword"""
		key_head = self.keyword_headlines()

		headlines = set()

		for headlinekw in key_head[kw]:
			content = headlinekw.headlineid.content
			headlines.add(content)

		return list(headlines)