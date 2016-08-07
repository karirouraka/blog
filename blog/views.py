from django.shortcuts import render, HttpResponse, render_to_response, RequestContext,redirect
from blog.models import BlogPost, BlogPostCategory, Comment, SearchKeyWords
from blog.forms import SearchForm, CommentsForm
from django.template import Context,Template
from django.template.loader import  render_to_string
# Create your views here.

def index_page(request):
    categories = BlogPostCategory.objects.all()
    new_posts = BlogPost.objects.all()[:2]
    search_form = SearchForm()
    return  render_to_response('post/base_page.html',{'categories':categories, 'new_posts':new_posts,'form':search_form},context_instance=RequestContext(request))

def get_post_by_category(request,category_pk):
    category = BlogPostCategory.objects.get(pk = category_pk)
    posts = category.posts.all()
    return  render_to_response('post/posts.html',{'posts':posts},context_instance=RequestContext(request))

def get_content_by_title(request,post_pk):
    post = BlogPost.objects.get(pk = post_pk)
    comments_form = CommentsForm()
    return render_to_response('post/post.html', {'post':post, 'comments_form':comments_form}, context_instance=RequestContext(request))

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

def search_by_key_words(request):
    needed_posts = []
    posts = BlogPost.objects.all()
    search_form = SearchForm(request.POST)
    if search_form.is_valid():
        search_form.save()
        d = search_form.cleaned_data
        key_words = d['keywords']
        key_words =   key_words.split()
        for key_word in key_words:
            for post in posts:
                if key_word in post.title or key_word in post.article:
                    needed_posts.append(post)
        return render_to_response('post/posts.html',{'posts':needed_posts,'form':search_form},context_instance=RequestContext(request))
    else :
        categories = BlogPostCategory.objects.all()
        new_posts = BlogPost.objects.all()[:2]
        return  render_to_response('base.html', {'categories': categories, 'new_posts': new_posts, 'form': search_form},
                           context_instance=RequestContext(request))

def send_comment(request, post_pk):
    post = BlogPost.objects.get(pk=post_pk)
    comment_form = CommentsForm(request.POST)
    if comment_form.is_valid():
        d = comment_form.cleaned_data
        answer = d['question'].lower()
        if answer == 'berlin':
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = 'blablabla'
            comment.save()
        return redirect('get_content_by_title', post_pk=post_pk)
    else:
        return render_to_response('post/post.html', {'post': post, 'comments_form': comment_form},
                                  context_instance=RequestContext(request))
