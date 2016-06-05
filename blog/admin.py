from django.contrib import admin
from blog.models import  BlogPost,BlogPostCategory
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    pass

class BlogPostCategoryAdmin(admin.ModelAdmin):
    pass



admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(BlogPostCategory,BlogPostCategoryAdmin)
