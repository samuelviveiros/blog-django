from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    DetailView,
    ListView,
)

from .models import Post


class PostList(ListView):
    template_name = 'pages/posts/list.html'

    def get_queryset(self):
        lookups = {}

        year = self.kwargs.get('year', None)
        month = self.kwargs.get('month', None)
        day = self.kwargs.get('day', None)

        if year:
            lookups.update(created_at__year=year)
        if month:
            lookups.update(created_at__month=month)
        if day:
            lookups.update(created_at__day=day)

        return Post.objects.filter(**lookups)


class PostDetail(DetailView):
    template_name = 'pages/posts/detail.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post, slug=slug)
