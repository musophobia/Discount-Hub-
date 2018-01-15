# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from olx.items import OlxItem
import re

class DarazSPSpider(scrapy.Spider):
	name = 'daraz'
	allowed_domains = ['daraz.com.bd']
	start_urls = ['https://www.daraz.com.bd/smartphones/',]
	prev_page='a'

	def parse(self,response):

		for ref in response.css('.sku.-gallery'):
			item=OlxItem()
			#item['title']=
			print('title')
			print('-'.join(ref.css('.link>.title ::text').extract()))
			item['title']='-'.join(ref.css('.link>.title ::text').extract())
			#print('url')
			print(ref.css('.link ::attr(href)').extract()[0])
			item['url']=ref.css('.link ::attr(href)').extract()[0]
			print('percentage')
			#item['percentage']=

			if (ref.css('.link>.price-container.clearfix>.sale-flag-percent ::text').extract()):
				print(ref.css('.link>.price-container.clearfix>.sale-flag-percent ::text').extract()[0])
				item['percentage']=ref.css('.link>.price-container.clearfix>.sale-flag-percent ::text').extract()[0]
			#else:
			#	print('no percentage')

			#item['old_price']=
				print('old_price')
				print((ref.css('.link>.price-container.clearfix>.price-box.ri>.price.-old ::text').extract()[2]).strip())
			#if len(ref.css('.link>.price-container.clearfix>.price-box.ri>.price.-old ::text').extract().length)>2

				item_old_price=(ref.css('.link>.price-container.clearfix>.price-box.ri>.price.-old ::text').extract()[2]).strip()
				x=re.findall('\\d+',item_old_price)
				y=x[0]+x[1]
				print(y)
				print("old_price")
				item['old_price']=y

			#else:
			#	print ('no old price')
			print('new_price')
			#item['new_price']=

			#if len(ref.css('.link>.price-container.clearfix>.price-box.ri>.price ::text').extract())>2:
			print(ref.css('.link>.price-container.clearfix>.price-box.ri>.price ::text').extract()[2].strip())
			item_new_price=(ref.css('.link>.price-container.clearfix>.price-box.ri>.price ::text').extract()[2]).strip()
			x=re.findall('\\d+',item_new_price)
			y=x[0]+x[1]
			print(y)
			print("new Price")
			item['new_price']=y
			#else:
			#	print('no new price')
			yield item

		
		next_page=response.css('.pagination>.osh-pagination.-horizontal ::attr(href)').extract()[-1]
		print(next_page)
		if self.prev_page==next_page:
			pass
		else:
			self.prev_page=next_page
			yield scrapy.Request(next_page, self.parse, dont_filter=True)