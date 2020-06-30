from .models import Headline, Headlinekeyword, Keyword, Newssource

class SentimentExtractor(object):
	"""docstring for SentimentExtractor"""
	def get_all_news_sources(self):
		"""Returns the labels and data needed to insert into visualization"""
		all_newsourcequeries = Newssource.objects.all()
		new_source_sentiment = {}
		labels = ['Positive', 'Negative', 'Neutral']
		for query in all_newsourcequeries:
			news_source = query.name
			new_source_sentiment[news_source] = self.get_percentage(news_source)
		return labels, new_source_sentiment

	def get_percentage(self, news_source):
		"""
		Returns the percentage of each
		"""
		p, ng, nu = self.get_sentiment_count(news_source)
		total = p + ng + nu
		return [100 * p/total, 100 * ng/total, 100 * nu/total]

	def get_sentiment_count(self, news_source):
		"""Takes in a news source string and gets the count"""
		idNews = Newssource.objects.get(name = news_source).id
		query_headlines = Headline.objects.filter(newssourceid = idNews)

		none_vals = query_headlines.filter(vader = None)
		pos_vals = query_headlines.filter(vader__gt=0)
		neg_vals = query_headlines.filter(vader__lt=0)
		neu_vals = query_headlines.filter(vader = 0)

		p, ng, nu = self.null_recount(none_vals, query_headlines)
		return [len(pos_vals) + p, len(neg_vals) + ng, len(neu_vals)+nu]

	def null_recount(self, query_null, query):
		"""Returns the number of negative positive and neutral values from null query"""
		pos, neg, neu = 0, 0, 0
		for q in query_null:
			val = self.get_sentiment_for_null(query, q.content)
			if val == None:
				continue

			if val ==1:
				pos+=1
			elif val == -1:
				neg +=1
			else:
				neu +=1
		return (pos, neg, neu)

	def get_sentiment_for_null(self, query, headline):
		"""
		Returns the sentiment value of the headline
		Returns None is there is no sentiment value at all
		"""
		headline0 = query.filter(content = headline)[0]

		if headline0.vader == None:
			return None 

		if headline0.vader > 0:
			return 1
		elif headline0.vader < 0:
			return -1
		else:
			return 0
