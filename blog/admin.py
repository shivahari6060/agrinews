from django.contrib import admin
from .models import Author, Post, Comment, Contact

# Register your models here.

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Contact)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email','created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'message')
    actions = ['approve_contacts']

    def approve_contacts(self, request, queryset):
        queryset.update(active=True)