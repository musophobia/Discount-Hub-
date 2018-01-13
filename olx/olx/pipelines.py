# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from discounts.models import Website,Product,ByPercentage
import re


class OlxPipeline(object):
    def process_item(self, item, spider):
        try:
            product = Product.objects.get(url=item['url'])
            print "Product already exist"
            return item
        except Product.DoesNotExist:
            pass
        
        percent50 = ByPercentage.objects.get(byPercentage=50)
        percent25 = ByPercentage.objects.get(byPercentage=25)
        website=Website.objects.get(website_name='pickaboo')
        product = Product()
        product.website = website
        product.title = item['title']
        product.price_old = item['old_price']
        product.price_new = item['new_price']
        product.percentage = item['percentage']
        if re.findall('\\d+',item['percentage']) > 50:
            product.byPercentage=percent50
        else:    
            product.byPercentage=percent25
        product.url = item['url']
       	product.save()
        return item

