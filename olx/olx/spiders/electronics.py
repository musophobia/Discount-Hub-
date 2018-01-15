# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from olx.items import OlxItem

class ElectronicsSpider(CrawlSpider):
	name = "pickaboo"
	#allowed_domains = ["www.olx.com.pk"]
	allowed_domains = ["www.pickaboo.com"]
	start_urls = [
		# 'https://www.olx.com.pk/computers-accessories/',
		#'https://www.olx.com.pk/tv-video-audio/',
		#'https://www.olx.com.pk/games-entertainment/'
		'https://www.pickaboo.com/mobile-tablet.html/',
		'https://www.pickaboo.com/daily-need.html/',
		'https://www.pickaboo.com/lifestyle-entertainment.html/',
		'https://www.pickaboo.com/computer-pc.html/',
		'https://www.pickaboo.com/electronics-appliances.html/',
	]

	rules = (
#        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
		Rule(LinkExtractor(allow=(), restrict_css=('.next.i-next',)),	
			callback="parse_item",
			follow=True),)

	def parse_item(self, response):
		item_links = response.css('.product-name ::attr(href)').extract()
		for a in item_links:
			yield scrapy.Request(a, callback=self.parse_detail_page)
	
	def parse_detail_page(self, response):
	#	title = response.css('h1::text').extract()[0].strip()
		title = response.css('.product-productname ::text').extract()[0].strip()
		old_price = response.css('.old-price > .price ::text').extract()[0].strip()
		new_price = response.css('.special-price > .price ::text').extract()[0].strip()
		#print(title)
		discount = response.css('.view-percent-price > strong ::text').extract()[0].strip()
		#price = response.css('.pricelabel > strong::text').extract()[0]
		#print(price)		
		item = OlxItem()
		item['title'] = title
		item['percentage'] = discount
		item['old_price'] = old_price
		item['new_price'] = new_price
		print("begin")
		print(title)
		print(discount)
		print(old_price)
		print(new_price)
		print("end")
	#	print(response.url)		
		item['url'] = response.url
		yield item
		
