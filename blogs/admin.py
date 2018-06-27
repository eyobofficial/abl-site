from django.contrib import admin
from . import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'get_full_name', )


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
    list_display = ('title', 'catagory', 'status', 'updated_at', )
    list_filter = ('status', 'open_for_comment', )
    search_fields = ('title', 'summary', 'content', )
    prepopulated_fields = {'slug': ('title', )}
    filter_horizontal = ('tags', )
