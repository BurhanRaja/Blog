from django.contrib import admin
from blog.models import Contact, Post, Categorie, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # class Media:
    #     js= ("https://cdn.tiny.cloud/1/8xr6gz7rijnldjasvvguc04k2tfk7frurcwg53xdsz77iffr/tinymce/5/tinymce.min.js",'javascript/tiny.js',)
    list_display = ('title', 'slug', 'post_category','created_on')
    search_fields = ['title', 'content', 'post_category']
    prepopulated_fields = {'slug': ('title',)}
    


admin.site.register(Post, PostAdmin)
admin.site.register((Categorie, Contact, Comment))