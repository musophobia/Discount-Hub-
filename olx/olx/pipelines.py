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
            print ("Product already exist")
            return item
        except Product.DoesNotExist:
            pass
        
        percent50 = ByPercentage.objects.get(byPercentage=50)
        percent25 = ByPercentage.objects.get(byPercentage=25)
        if item['url'].find("daraz")!=-1:
        #if any("daraz" in s for s in item['url']):
            website=Website.objects.get(website_name='daraz')
        else:
            website=Website.objects.get(website_name='pickaboo')
        product = Product()
        product.website = website
        if item['title']:
            product.title = item['title'].encode('ascii', 'ignore').decode('ascii')
        if item['old_price']:
            product.price_old = item['old_price'].encode('ascii', 'ignore').decode('ascii')
        if item['new_price']:
            product.price_new = item['new_price'].encode('ascii', 'ignore').decode('ascii')
        if item['percentage']:
            product.percentage = item['percentage'].encode('ascii', 'ignore').decode('ascii')
        #if re.findall('\\d+',item['percentage']) > 50:
        product.byPercentage=percent50
        #else:    
        #product.byPercentage=percent25
        product.url = item['url']
        #if re.findall('\\d+',item['percentage']) > 10:
        if item['percentage']:
       	    product.save()
        else:
            pass
        return item

