from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404

from . import models
from .forms import CommentForm


class CatagoryDetail(DetailView):
    model = models.Catagory
    template_name = 'blogs/posts.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['post_list'] = self.object.posts.published()
        context['popular_posts'] = models.Post.objects.popular()[:4]
        context['catagory_list'] = models.Catagory.objects.all()
        context['post_count'] = models.Post.objects.published().count()
        context['page'] = 'blogs'
        return context


class PostList(ListView):
    model = models.Post
    template_name = 'blogs/posts.html'

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.published().order_by('-created_at')[:4]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['popular_posts'] = self.model.objects.popular()[:4]
        context['catagory_list'] = models.Catagory.objects.all()
        context['post_count'] = models.Post.objects.published().count()
        context['page'] = 'blogs'
        return context


def post_detail(request, pk, slug):
    post = get_object_or_404(models.Post, pk=pk, slug=slug)
    form_class = CommentForm
    template_name = 'blogs/post-detail.html'

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blogs:post-detail', pk=pk, slug=slug)
    else:
        form = form_class()
        popular_posts = models.Post.objects.popular()[:4]
        catagory_list = models.Catagory.objects.all()
        post_count = models.Post.objects.published().count()

    return render(request, template_name, {
        'post': post,
        'form': form,
        'popular_posts': popular_posts,
        'catagory_list': catagory_list,
        'post_count': post_count,
        'page': 'blogs',
    })
