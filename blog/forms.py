# -*- coding: utf-8 -*-
from django import  forms
from blog.models import SearchKeyWords, Comment

class SearchForm(forms.ModelForm):
    # search = forms.CharField(label=u'Поиск')

    class Meta:
        model = SearchKeyWords
        fields = '__all__'





class CommentsForm(forms.ModelForm):
    # comment = forms.CharField()
    #author = forms.CharField(label=u'Автор')
    question = forms.CharField(label=u'Столица Германии?')

    class Meta:
        model = Comment
        fields = ['text']