from django.contrib import admin
from blog.models import  BlogPost,BlogPostCategory, Comment, SearchKeyWords
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    pass

class BlogPostCategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class SearchKeyWordsAdmin(admin.ModelAdmin):
    pass


admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(BlogPostCategory,BlogPostCategoryAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(SearchKeyWords, SearchKeyWordsAdmin)