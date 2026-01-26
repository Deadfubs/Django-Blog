from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="home"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug>", views.post_datail, name="post-datails")
]
