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


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'sent_date', 'is_seen', ]
    search_fields = ['name', 'email', 'subject', ]
    readonly_fields = ['name', 'email', 'subject', 'content', 'sent_date', ]
    exclude = ['is_seen']

    def get_form(self, request, obj, *args, **kwargs):
        if obj and obj.is_seen is False:
            obj.is_seen = True
            obj.save()
        return super().get_form(request, obj, *args, **kwargs)
