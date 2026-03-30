from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Post
from .serializer import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
# Create Post List Endpoints that allows users to 
# - view ALL blog posts
# - create new blog posts
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    filterset_fields = ['author', 'date_created']
    
# automatically assigned the post to the logged-in user
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Only user who created a post should be able to:
#   - update it
#   - delete it
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Let anyone view posts
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

# Create Post Detail Endpoints that allows users to 
# - view a single post
# - update a post
# - delete a post
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]



