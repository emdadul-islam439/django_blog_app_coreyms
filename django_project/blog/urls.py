from django.contrib import admin
from django.urls import path
from blog.views import PostListview
from blog import views

urlpatterns = [
    # path("", views.home, name = "blog-home"),
    path("", PostListview.as_view(), name = "blog-home"),
    path("about/", views.about, name = "blog-about")
]
