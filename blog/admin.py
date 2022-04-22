from django.contrib import admin
from blog.models import Contact, Post, Categorie, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'post_category','created_on')
    search_fields = ['title', 'content', 'post_category']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register((Categorie, Contact, Comment))