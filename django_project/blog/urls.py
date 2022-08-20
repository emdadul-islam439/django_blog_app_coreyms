from django.contrib import admin
from django.urls import path
from blog.views import (
    PostListview, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListview
)
from blog import views

urlpatterns = [
    # path("", views.home, name = "blog-home"),
    path("", PostListview.as_view(), name = "blog-home"),
    path("user/<str:username>", UserPostListview.as_view(), name = "user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name = "post-detail"),
    path("post/new/", PostCreateView.as_view(), name = "post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name = "post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name = "post-delete"),
    path("about/", views.about, name = "blog-about")
]
