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
from django.conf.urls import url,include
from django.contrib import admin
from blog.views import index_page,get_post_by_category, get_content_by_title

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_page,name='index_page'),
    url(r'^get_post_by_category/(?P<category_pk>\d+)/$',get_post_by_category,name='get_post_by_category'),
    url(r'^get_content_by_title/(?P<post_pk>\d+)/$', get_content_by_title, name='get_content_by_title'),
    #url(r'^',include('numbers_app.urls')),
    # url(r'^fill_out',fill_out, name='fill_out'),
    # url(r'^calc/$', calculations, name='calc'),
    # url(r'^min/$', minimal, name='minimal'),
    # url(r'^substitute/$', substitute, name = 'substitute'),
    # url(r'^delete_small/$', 'numbers_app.views.delete_small', name='delete'),
]
