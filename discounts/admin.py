# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Website, Product, ByPercentage, Coupon


# Register your models here.

admin.site.register(Website)
admin.site.register(Product)
admin.site.register(ByPercentage)
admin.site.register(Coupon)