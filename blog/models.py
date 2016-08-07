# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models




class BlogPostCategory(models.Model):
    title = models.CharField(max_length=200,verbose_name=u'Название')
    description = models.TextField(verbose_name=u'Описание')



    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    article = models.TextField()
    date = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    is_publish = models.BooleanField(default= False)
    image  = models.ImageField(null=True,blank=True,upload_to="images")
    cat = models.ManyToManyField(BlogPostCategory,related_name ="posts")


    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return   self.title + " "+ str(self.likes)

    def increase_likes(self):
        self.likes += 1
        self.save()

    def get_short_description(self):
        short_description = self.article[:200] + '...'
        return short_description

    def decrease_likes(self):
        if self.likes > 0:
            self.likes -= 1
            self.save()

    def count_comments(self):
        return self.comments.filter(publish=True).count()




class Comment(models.Model):
    author = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(BlogPost, related_name="comments")
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.author + ' ' + self.text[:20]


class SearchKeyWords(models.Model):
    keywords = models.CharField(max_length=300)

    def __str__(self):
        return self.keywords