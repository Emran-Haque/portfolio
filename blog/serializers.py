from rest_framework import serializers
from .models import Blog


class BlogListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'author', 'publish_date',
            'description', 'image', 'tags', 'featured',
        ]


class BlogDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

    class Meta:
        model = Blog
        fields = '__all__'
