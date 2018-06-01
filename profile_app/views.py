# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from registration.backends.default.views import RegistrationView
from .forms import ProfileForm
from .models import Profile
from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.

class ProfileHome(View):
	"""docstring for ProfileHome"""
	

	def get(self, request):
		template_name = 'index.html'
		context_instance = RequestContext(request)
		context = {'user':request.user}
		return render_to_response(template_name,context, context_instance) 
		

class MyRegistrationView(RegistrationView):

    form_class = ProfileForm

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)
        p = form_class.cleaned_data['passport']
        new_profile = Profile.objects.create(user=new_user, passport=p)
        new_profile.save()
        return new_user