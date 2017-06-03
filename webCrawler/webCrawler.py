import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
	page = 1
	while page < max_pages:
		url = 'https://www.amazon.com.br/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3APS4&page='+str(page)+'&keywords=PS4&ie=UTF8&qid=1496517145'
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text)
		for link in soup.findAll('a', {'class', 'a-link-normal'}):
			href = link.get('href')
			title = link.get('title')
			get_single_item_data(href)
		page += 1

# def get_single_item_data(url):
# 	source_code = requests.get(url)
# 	plain_text = source_code.text
# 	soup = BeautifulSoup(plain_text, "html.parser")
# 	for link in soup.findAll('input', {'name', 'amzn-r'}):
# 		print('hello?')



# get_single_item_data('https://www.amazon.com.br/PlayStation-Ultimate-Master-Console-English-ebook/dp/B00GNJ3YH8/ref=sr_1_1?ie=UTF8&qid=1496517184&sr=8-1&keywords=PS4')

#CHECK SCRAPPY vs Beautiful SOup 4