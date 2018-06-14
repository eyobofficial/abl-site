from django.shortcuts import get_object_or_404,
from django.views.generic import TemplateView

from . import models


class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['brand'] = get_object_or_404(models.Brand, pk=1)
        context['slide_list'] = models.Slide.objects.all()
        context['widget_list'] = models.Widget.objects.all()
        context['service_list'] = models.Service.objects.filter(featured=True)
        context['testimonial_list'] = models.Testimonial.objects.filter(
            featured=True
        )
        context['client_list'] = models.Client.objects.filter(featured=True)
        context['page'] = 'home'
        return context


class AboutView1(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = 'about'
        return context


class ServiceView1(TemplateView):
    template_name = 'pages/service.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = 'service'
        return context


class ContactView1(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = 'contact'
        return context