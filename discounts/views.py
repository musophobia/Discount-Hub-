# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from .models import Website,Product,ByPercentage,Coupon, Profile
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views.generic.detail import DetailView
from .forms import UserForm
from django.contrib.auth.models import User
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def redirect_root(request):
	return HttpResponseRedirect('/discounts/')

class IndexView(generic.ListView):
	template_name='discounts/index.html'
	context_object_name='all_websites'
	def get_queryset(self):
		return Website.objects.all()

class IndexView2(generic.ListView):
	template_name='discounts/index2.html'
	context_object_name='all_bypercentages'
	def get_queryset(self):
		return ByPercentage.objects.all()
						
@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):
	model=Website
	template_name='discounts/detail.html'

	
@method_decorator(login_required, name='dispatch')
class DetailView2(generic.DetailView):
	model=ByPercentage
	template_name='discounts/detail2.html'
		

	
class CouponCreate(CreateView):
	model = Coupon
	fields = ['coupon_name','coupon_detail','coupon_code','coupon_link']

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.created_by = self.request.user
		self.object.save()
		return super(ModelFormMixin, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class CouponDetail(DetailView):
	model = Coupon
	template_name='discounts/coupondetail.html'

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)
		edit_user=Profile.objects.get(user=self.object.created_by)
		if self.object.created_by!=self.request.user:
			edit_user.credit_available+=10
		edit_user.save()

		decrease_self= self.request.user
		if self.object.created_by!=self.request.user:
			decrease_self.profile.credit_available-=20
		decrease_self.save()

		return self.render_to_response(context)

class CouponUpdate(UpdateView):
	model = Coupon
	fields = ['coupon_name','coupon_detail']

class CouponDelete(DeleteView):
	model = Coupon
	success_url=reverse_lazy('discounts:coupon')

class CouponView(generic.ListView):
	template_name='discounts/coupon.html'
	context_object_name='all_coupons'
	def get_queryset(self):
		return Coupon.objects.all()




class UserFormView(View):
	form_class= UserForm
	template_name='discounts/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			#cleaned (normalized) data

			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user=authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('discounts:index')

		return render(request, self.template_name, {'form': form})

"""
def index(request):
	all_websites = Website.objects.all()
	all_discounts = ByPercentage.objects.all()
	#########way 2
	#template = loader.get_template('discounts/index.html')
	######way 1
	#html = ''
	#for website in all_websites:
	#	url = '/discounts/' + str(website.id) + '/'
	#	html += '<a href="' + url + '">' + website.website_name + '</a><br>'
	##########way 3
	context = {
		'all_websites' : all_websites,
		'all_discounts' : all_discounts,
	}
	##way 2###return HttpResponse(template.render(context, request))
	return render(request,'discounts/index.html', context)

def detail(request, website_id):
	#return HttpResponse("<h2>All website names here "+ str(website_id) +"</h2>")
	#try:
	#	website = Website.objects.get(pk=website_id)
	#except Website.DoesNotExist:
	#	raise Http404("Not so many websites scrapped yet bro!!")	
	website = get_object_or_404(Website, pk=website_id)
	return render(request, 'discounts/detail.html', {'website': website})

	

def favorite(request, website_id):	
	website = get_object_or_404(Website, pk=website_id)
	try:
		selected_product= website.product_set.get(pk=request.POST['product'])
	except (KeyError, Product.DoesNotExist):
		return render(request, 'discounts/detail.html',{
			'website':website,
			'error_message:' :"you did not select valid ",
			})
	else:
		selected_product.is_favorite= True
		selected_product.save()
		return render(request, 'discounts/detail.html', {'website': website})

"""


