from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class PostsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'posts-list'


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'