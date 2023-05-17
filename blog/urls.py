from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("posts/", views.get_all_posts, name="posts"),
    path("create-post/", views.create_post, name="create-posts"),
    path("post/<int:id>", views.get_post_by_id, name="post"),
    path("post/<int:id>/comments/", views.comment, name="comments"),
]