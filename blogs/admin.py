from django.contrib import admin
from . import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'get_full_name', )


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', '-updated_at', )
    search_fields = ('full_name', 'title', 'bio', )


@admin.register(models.Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', )
    search_fields = ('title', 'description', )
    prepopulated_fields = {'slug': ('title', )}


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title', )}


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'catagory', 'author', 'status', 'updated_at', )
    list_filter = ('status', 'open_for_comment', 'author', )
    search_fields = ('title', 'summary', 'content', )
    prepopulated_fields = {'slug': ('title', )}
    filter_horizontal = ('tags', )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'post', 'is_approved', 'updated_at', )
    list_filter = ('is_approved', )
    search_fields = ('full_name', 'content', )
