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
        
        try:
            percent90 = ByPercentage.objects.get(byPercentage=90)
        except ByPercentage.DoesNotExist:
            percent90=ByPercentage(byPercentage=90)
            percent90.save()        

        try:
            percent70 = ByPercentage.objects.get(byPercentage=70)
        except ByPercentage.DoesNotExist:
            percent70=ByPercentage(byPercentage=70)
            percent70.save()

        try:
            percent50 = ByPercentage.objects.get(byPercentage=50)
        except ByPercentage.DoesNotExist:
            percent50=ByPercentage(byPercentage=50)
            percent50.save()

        try:
            percent30 = ByPercentage.objects.get(byPercentage=30)
        except ByPercentage.DoesNotExist:
            percent30=ByPercentage(byPercentage=30)
            percent30.save()

        try:
            percent15 = ByPercentage.objects.get(byPercentage=15)
        except ByPercentage.DoesNotExist:
            percent15=ByPercentage(byPercentage=15)
            percent15.save()

        try:
            percent5 = ByPercentage.objects.get(byPercentage=5)
        except ByPercentage.DoesNotExist:
            percent5=ByPercentage(byPercentage=5)
            percent5.save()

        if item['url'].find("daraz")!=-1:
        #if any("daraz" in s for s in item['url'])
            try:
                website=Website.objects.get(website_name='daraz')
            except Website.DoesNotExist:
                website=Website(website_name='daraz',website_region='BD')
                website.save()
        else:
            try:
                website=Website.objects.get(website_name='pickaboo')
            except Website.DoesNotExist:
                website=Website(website_name='pickaboo',website_region='BD')
                website.save()
        
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
        product.url = item['url']

        print("asdfasdfasdfasdfasdfsdafasdlk;kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        results=((re.findall('\d+', item['percentage'])))
        print((re.findall('\d+', item['percentage'])))
        print("asdfasdfasdfasdfasdfsdafasdlk;kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

        results = map(int, results)

        print("this is results")
        print(results[0])
        print("this was results")


        if results[0] > 50:
            product.byPercentage=percent50
            product.save()
        elif results[0] > 30:
            product.byPercentage=percent30
            product.save()
        elif results[0] > 15:
            product.byPercentage=percent15
            product.save()
        elif results[0] > 5:
            product.byPercentage=percent5
            product.save()
        #else:    
        #product.byPercentage=percent25
        
        #if re.findall('\\d+',item['percentage']) > 10:
        
        return item

