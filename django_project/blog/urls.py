from django.contrib import admin
from django.urls import path
from blog.views import PostListview, PostDetailView
from blog import views

urlpatterns = [
    # path("", views.home, name = "blog-home"),
    path("", PostListview.as_view(), name = "blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name = "post-detail"),
    path("about/", views.about, name = "blog-about")
]
