from django.shortcuts import render, HttpResponse, render_to_response, RequestContext
from blog.models import BlogPost, BlogPostCategory
from django.template import Context,Template
from django.template.loader import  render_to_string
# Create your views here.

def index_page(request):
    categories = BlogPostCategory.objects.all()
    return  render_to_response('base.html',{'categories':categories},context_instance=RequestContext(request))

def get_post_by_category(request,category_pk):
    category = BlogPostCategory.objects.get(pk = category_pk)
    posts = category.posts.all()
    return  render_to_response('post/posts.html',{'posts':posts},context_instance=RequestContext(request))

def get_content_by_title(request,post_pk):
    post = BlogPost.objects.get(pk = post_pk)
    return render_to_response('post/post.html', {'post':post}, context_instance=RequestContext(request))