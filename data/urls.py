"""data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include,patterns
from django.contrib import admin
from blog.views import index_page,get_post_by_category, get_content_by_title, increase_likes,success_vote, decrease_likes, \
    search_by_key_words, send_comment

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_page,name='index_page'),
    url(r'^get_post_by_category/(?P<category_pk>\d+)/$',get_post_by_category,name='get_post_by_category'),
    url(r'^get_content_by_title/(?P<post_pk>\d+)/$', get_content_by_title, name='get_content_by_title'),
    url(r'^increase_likes/(?P<post_pk>\d+)/$', increase_likes, name='increase_likes'),
    url(r'^success_vote/(?P<post_pk>\d+)/$', success_vote, name='success_vote'),
    url(r'^decrease_likes/(?P<post_pk>\d+)/$', decrease_likes, name='decrease_likes'),
    url(r'^search_by_key_words/$', search_by_key_words, name='search_by_key_words'),
    url(r'^send_comment/(?P<post_pk>\d+)/$', send_comment, name='send_comment'),
    #url(r'^',include('numbers_app.urls')),
    # url(r'^fill_out',fill_out, name='fill_out'),
    # url(r'^calc/$', calculations, name='calc'),
    # url(r'^min/$', minimal, name='minimal'),
    # url(r'^substitute/$', substitute, name = 'substitute'),
    # url(r'^delete_small/$', 'numbers_app.views.delete_small', name='delete'),
]
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
