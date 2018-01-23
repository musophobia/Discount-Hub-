# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse 
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    credit_available = models.IntegerField(default=1000)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()


class ByPercentage(models.Model):
	byPercentage = models.CharField(max_length=250)
	def __str__(self):
		return self.byPercentage 
		
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
	#coupon_submit = models.CharField(max_length=250)
	coupon_name = models.CharField(max_length=250)
	coupon_detail = models.CharField(max_length=2500)
	coupon_code = models.CharField(max_length=2500)
	coupon_link = models.CharField(max_length=2500)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	def get_absolute_url(self):
		return reverse('discounts:coupon')

