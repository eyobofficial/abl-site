from django.views.generic import ListView, DetailView
from . import models


class CatagoryDetail(DetailView):
    model = models.Catagory
    template_name = 'blogs/blogs.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['post_list'] = self.object.posts.published()
        context['popular_posts'] = models.Post.objects.popular()[:4]
        context['catagory_list'] = models.Catagory.objects.all()
        context['page'] = 'blogs'
        return context


class PostList(ListView):
    model = models.Post
    template_name = 'blogs/blogs.html'

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.published().order_by('-created_at')[:4]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['popular_posts'] = self.model.objects.popular()[:4]
        context['catagory_list'] = models.Catagory.objects.all()
        context['page'] = 'blogs'
        return context


class PostDetail(DetailView):
    model = models.Post
    template_name = 'blogs/blog-detail.html'

    def get_context_data(self, *args, **kwargs):
        self.object.update_read_count()
        context = super().get_context_data(*args, **kwargs)
        context['page'] = 'blogs'
        return context
