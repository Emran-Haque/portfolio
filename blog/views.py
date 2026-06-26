from rest_framework import generics
from .models import Blog, Comment
from .serializers import BlogListSerializer, BlogDetailSerializer, CommentSerializer


class BlogListView(generics.ListAPIView):
    serializer_class = BlogListSerializer

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).order_by('-publish_date')


class BlogDetailView(generics.RetrieveAPIView):
    serializer_class = BlogDetailSerializer
    lookup_field = 'slug'
    queryset = Blog.objects.filter(is_published=True)


class FeaturedBlogsView(generics.ListAPIView):
    serializer_class = BlogListSerializer
    pagination_class = None

    def get_queryset(self):
        return Blog.objects.filter(is_published=True, featured=True).order_by('-publish_date')[:3]


class RelatedBlogsView(generics.ListAPIView):
    serializer_class = BlogListSerializer
    pagination_class = None

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Blog.objects.filter(is_published=True).exclude(slug=slug).order_by('-publish_date')[:3]


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    pagination_class = None

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Comment.objects.filter(blog__slug=slug)

    def perform_create(self, serializer):
        slug = self.kwargs.get('slug')
        blog = Blog.objects.get(slug=slug, is_published=True)
        serializer.save(blog=blog)
