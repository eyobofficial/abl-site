from django.views.generic import ListView, DetailView
from . import models


class BlogList(ListView):
    model = models.Post
    template_name = 'blogs/blogs.html'

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.published().order_by('-created_at')[:4]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['popular_posts'] = self.model.objects.popular()[:4]
        context['page'] = 'blogs'
        return context


class BlogDetail(DetailView):
    model = models.Post
    template_name = 'blogs/blog-detail.html'

    def get_context_data(self, *args, **kwargs):
        self.object.update_read_count()
        context = super().get_context_data(*args, **kwargs)
        context['page'] = 'blogs'
        return context
