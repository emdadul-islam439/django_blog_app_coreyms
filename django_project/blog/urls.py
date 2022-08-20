from django.contrib import admin
from django.urls import path
from blog.views import (
    PostListview, 
    PostDetailView, 
    PostCreateView
)
from blog import views

urlpatterns = [
    # path("", views.home, name = "blog-home"),
    path("", PostListview.as_view(), name = "blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name = "post-detail"),
    path("post/new/", PostCreateView.as_view(), name = "post-create"),
    path("about/", views.about, name = "blog-about")
]
