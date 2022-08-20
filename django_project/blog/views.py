from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/index.html", context)


class PostListview(ListView):
    model = Post
    template_name: str = "blog/home.html"    #<app>/<model>_<viewtype>.html
    context_object_name: str = "posts"
    ordering = ['-date_posted']


def about(request):
    return render(request, "blog/about.html", {"title" : "About"})
