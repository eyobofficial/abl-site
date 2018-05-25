from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'pages/index.html'


class HomeView1(TemplateView):
    template_name = 'p1/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = 'home'
        return context


class AboutView1(TemplateView):
    template_name = 'p1/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = 'about'
        return context


class ServiceView1(TemplateView):
    template_name = 'p1/service.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = 'service'
        return context


class ContactView1(TemplateView):
    template_name = 'p1/contact.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = 'contact'
        return context


class BlogsView1(TemplateView):
    template_name = 'p1/blogs.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = 'blogs'
        return context


class BlogDetailView1(TemplateView):
    template_name = 'p1/blog-detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = 'blogs'
        return context