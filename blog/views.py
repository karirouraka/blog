from django.shortcuts import render, HttpResponse, render_to_response, RequestContext
from blog.models import BlogPost, BlogPostCategory
from django.template import Context,Template
from django.template.loader import  render_to_string
# Create your views here.

def git_test(request):
    return HttpResponse()


