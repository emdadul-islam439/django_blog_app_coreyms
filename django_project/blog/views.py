from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/index.html", context)


class PostListview(ListView):
    model = Post
    template_name: str = "blog/index.html"  # <app>/<model>_<viewtype>.html
    context_object_name: str = "posts"
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
