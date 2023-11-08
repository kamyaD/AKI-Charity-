from django.contrib import admin
from .models import Contacts,BlogPost, Comment, Category

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message')
admin.site.register(Contacts,ContactAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','author','date','text')
admin.site.register(BlogPost,BlogPostAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('comment_title','author','text','created_at')

    def comment_title(self,obj):
        return obj.post.title
admin.site.register(Comment,CommentsAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category,categoryAdmin)


