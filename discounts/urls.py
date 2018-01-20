from django.conf.urls import url

from . import views


app_name = 'discounts'

urlpatterns = [
	# /discounts/
	url(r'^$', views.IndexView.as_view(), name='index'),

	url(r'percent/$',views.IndexView2.as_view(), name='index2'),

	# /discounts/22
	url(r'^register/$', views.UserFormView.as_view(), name='register'),

	url(r'product/(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),

	url(r'percent/(?P<pk>[0-9]+)/$',views.DetailView2.as_view(), name='detail2'),
	
	###
	url(r'coupon/$',views.CouponView.as_view(), name='coupon'),
	##
	#url(r'coupon/^(?P<pk>[0-9]+)$',views.CouponView.as_view(), name='coupon'),
	#discounts/coupons/add
	url(r'coupon/add/$',views.CouponCreate.as_view(), name='coupon-add'),
	url(r'coupon/(?P<pk>[0-9]+)/update$',views.CouponUpdate.as_view(), name='coupon-update'),
	url(r'coupon/(?P<pk>[0-9]+)/delete/$',views.CouponDelete.as_view(), name='coupon-delete'),
	url(r'coupon/(?P<pk>[0-9]+)/detail/$',views.CouponDetail.as_view(), name='coupon-detail'),

]
