import scrapy 

class QuotesSpider(scrapy.Spider):
	name = "quotes"
	
	def start_requests(self):
		urls = [
			'http://quotes.toscrape.com/page/1/', 
			'http://quotes.toscrape.com/page/2/', 
		]

		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	def parse(self, response):
		if 0: 
			page = response.url.split("/")[-2]
			filename = 'quotes-%s.html' % page 
			with open(filename, 'wb') as f:
				f.write(response.body)
			self.log('Save file %s' % filename)

		for quote in response.css('div.quote'):
			# print(quote.css('span.text::text').get())
			d = {
				'text': quote.css('span.text::text').get(), 
				'author': quote.css('small.author::text').get(), 
				'tags': quote.css('div.tags a.tag::text').getall(), 
				}
			yield d

		next_page = response.css('li.next a::attr(href)').get()
		if next_page is not None: 
			next_page = response.urljoin(next_page)
			print(next_page)
			yield scrapy.Request(next_page, callback=self.parse)