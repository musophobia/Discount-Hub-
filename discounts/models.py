# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse 
from django.db import models

# Create your models here.

class ByPercentage(models.Model):
	byPercentage = models.CharField(max_length=250)

class Website(models.Model):
	website_name = models.CharField(max_length=25)
	website_region = models.CharField(max_length=25)

	def __str__(self):
		return self.website_name + ' - ' + self.website_region

class Product(models.Model):
	website = models.ForeignKey(Website, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	percentage = models.CharField(max_length=25)
	price_old = models.CharField(max_length=25)
	price_new = models.CharField(max_length=25)
	url = models.CharField(max_length=2000)
	is_favortie = models.BooleanField(default=False)
	byPercentage = models.ForeignKey(ByPercentage, on_delete=models.CASCADE)

	class Meta:
		ordering = ['-pk']


	def __str__(self):
		return self.title

class Coupon(models.Model):
	coupon_name = models.CharField(max_length=250)
	coupon_detail = models.CharField(max_length=2500)
	def get_absolute_url(self):
		return reverse('discounts:coupon')

