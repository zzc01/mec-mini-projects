# Web Scraping Using Scrapy Spider 

- Use Scrapy spider to crawl quotes.toscrape.com 
- Use CSS selector 
- Use XPATH selector 
- Recursively follow the next link to scrap the pages 
- Store the quotes into JSON file 
- Load the JSON file data into Sqlite3 database 

## Files
- quotes_xpath_spider.py 
The scaping script using XPATH selector 
- quotes_spider.py
The scaping script using CSS selector 
- quotes_xpath.json
JSON file collected using XPATH selector with quotes_xpath_spider.py 
- quotes.json
JSON file collected using CSS selector with quotes_spider.py 
- quotes.db
Sqlite3 database
- jsonToSqlLite3.ipynb
Is used to load the JSON file into Sqlite3 database 