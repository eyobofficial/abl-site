from django.contrib import admin
from . import models


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at', ]


@admin.register(models.Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at', ]


@admin.register(models.Widget)
class WidgetAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at', ]


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'updated_at', ]


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at', 'featured', ]
    list_filter = ['featured', ]


@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = [
        'client', 'position', 'title',
        'featured', 'updated_at', 'featured',
    ]
    list_filter = ['featured', ]


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'updated_at', 'featured', ]
    list_filter = ['featured', ]


@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at']
