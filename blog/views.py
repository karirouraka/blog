from django.shortcuts import render, HttpResponse, render_to_response, RequestContext,redirect
from blog.models import BlogPost, BlogPostCategory
from django.template import Context,Template
from django.template.loader import  render_to_string
# Create your views here.

def index_page(request):
    categories = BlogPostCategory.objects.all()
    new_posts = BlogPost.objects.all()[:2]

    return  render_to_response('base.html',{'categories':categories, 'new_posts':new_posts},context_instance=RequestContext(request))

def get_post_by_category(request,category_pk):
    category = BlogPostCategory.objects.get(pk = category_pk)
    posts = category.posts.all()
    return  render_to_response('post/posts.html',{'posts':posts},context_instance=RequestContext(request))

def get_content_by_title(request,post_pk):
    post = BlogPost.objects.get(pk = post_pk)
    return render_to_response('post/post.html', {'post':post}, context_instance=RequestContext(request))

def success_vote(request, post_pk):
    return render_to_response('post/success_vote.html',{'post_pk':post_pk},context_instance=RequestContext(request))

def increase_likes(request,post_pk):
    post = BlogPost.objects.get(pk=post_pk)
    post.increase_likes()
    return redirect ('success_vote',post_pk= post_pk)

def decrease_likes(request, post_pk):
    post = BlogPost.objects.get(pk=post_pk)
    post.decrease_likes()
    return redirect ('success_vote',post_pk=post_pk)
