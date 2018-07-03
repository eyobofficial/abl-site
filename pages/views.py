from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import TemplateView, CreateView

from . import models
from . import forms


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


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['brand'] = get_object_or_404(models.Brand, pk=1)
        context['staff_list'] = models.Staff.objects.all()
        context['client_list'] = models.Client.objects.all()
        context['page'] = 'about'
        return context


class ServiceView(TemplateView):
    template_name = 'pages/service.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['brand'] = get_object_or_404(models.Brand, pk=1)
        context['service_list'] = models.Service.objects.all()
        context['testimonal_list'] = models.Testimonial.objects.all()
        context['page'] = 'service'
        return context


class ContactViewOld(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['brand'] = get_object_or_404(models.Brand, pk=1)
        context['page'] = 'contact'
        return context


class ContactView(CreateView):
    model = models.Message
    template_name = 'pages/contact.html'
    success_url = '/contact/'
    form_class = forms.ContactForm

    def form_valid(self, form, *args, **kwargs):
        messages.success(
            self.request,
            'Thank you for your feedback!'
        )
        return super().form_valid(form, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['brand'] = get_object_or_404(models.Brand, pk=1)
        context['page'] = 'contact'
        return context


def subscribe(request):
    redirect_url = request.POST.get('next', '/')
    redirect_url += '#page-footer'

    if request.method == 'POST':
        form = forms.SubscriberForm(request.POST)
        messages.success(
            request,
            'Thank you for subscribing to our news and latest blogs!'
        )

        if form.is_valid():
            form.save()
    return redirect(redirect_url)
