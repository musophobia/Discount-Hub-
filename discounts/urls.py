from django.conf.urls import url

from . import views


app_name = 'discounts'

urlpatterns = [
	# /discounts/
	url(r'^$', views.IndexView.as_view(), name='index'),

	# /discounts/22
	url(r'^register/$', views.UserFormView.as_view(), name='register'),

	url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
	
	###
	url(r'coupon/$',views.CouponView.as_view(), name='coupon'),
	##
	#url(r'coupon/^(?P<pk>[0-9]+)$',views.CouponView.as_view(), name='coupon'),
	#discounts/coupons/add
	url(r'coupon/add/$',views.CouponCreate.as_view(), name='coupon-add'),
	url(r'coupon/(?P<pk>[0-9]+)/$',views.CouponUpdate.as_view(), name='coupon-update'),
	url(r'coupon/(?P<pk>[0-9]+)/delete/$',views.CouponDelete.as_view(), name='coupon-delete'),
]
