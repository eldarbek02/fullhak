from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Like
from post.serializers import PostSerializer


class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    post = PostSerializer(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        return self.Meta.model.objects.create(author=user, **validated_data)