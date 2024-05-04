from django.urls import path
from . import views

urlpatterns = [
    path("comments/", views.CreateCommentView.as_view(), name="comment-list"),
    path("comments/delete/<iny:pk", views.CommentDelete.as_view(), name="delete-comment")
]
