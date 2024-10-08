from django.urls import path
from .views import PostDetailView, PostListCreateView, CommentListCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name="post_list_create"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('posts/<int:pk>/comments/', CommentListCreateView.as_view(), name="post_list_create")
]
