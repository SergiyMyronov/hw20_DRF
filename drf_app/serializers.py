from drf_app.models import Comment, Post

from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'header',
            'short_description',
            'image',
            'description',
            'is_active',
        ]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'text',
            'is_published',
            'post',
        ]
