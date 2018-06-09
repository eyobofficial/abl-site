from django.shortcuts import render
from django.views.generic import TemplateView


class BlogList(TemplateView):
    template_name = 'blogs/blogs.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = 'blogs'
        return context


class BlogDetail(TemplateView):
    template_name = 'blogs/blog-detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = 'blogs'
        return context
