import scrapy 

class QuotesSpider(scrapy.Spider):
	name = "quotes_xpath"
	
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

		for quote in response.xpath('//div[@class="quote"]'): 
			d = {
				'text': quote.xpath('.//span[@class="text"]/text()').get(), 
				'author': quote.xpath('.//small[@class="author"]/text()').get(), 
				'tags': quote.xpath('.//a[@class="tag"]/text()').getall(), 
				}
			yield d

		next_page = response.xpath('//li[@class="next"]//a/@href').get()
		if next_page is not None: 
			next_page = response.urljoin(next_page)
			print(next_page)
			yield scrapy.Request(next_page, callback=self.parse)