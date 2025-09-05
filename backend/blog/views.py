from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    只读 API：获取文章列表和详情
    """
    queryset = Post.objects.filter(is_published=True).select_related('category').prefetch_related('tags')
    serializer_class = PostSerializer