# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.shortcuts import render


# # Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse(" we are comming soon")

from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('content/index.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))