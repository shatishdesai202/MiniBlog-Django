from django.contrib import admin
from .models import Post, Contact
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'desc', 'post_by']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ['name', 'phone', 'message', 'email']