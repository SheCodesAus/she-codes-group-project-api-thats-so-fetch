from rest_framework import serializers
from .models import Articles, Category, Comment
from django.contrib.auth import get_user_model
from users.models import CustomUser

User = get_user_model()


class CommentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    articles_id = serializers.IntegerField()
    # supporter = serializers.ReadOnlyField(source='supporter.id')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

class CommentDetailSerializer(CommentSerializer):
    
    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.articles_id = validated_data.get('articles_id', instance.articles_id)
        # instance.supporter = validated_data.get('supporter', instance.supporter_id)
        return instance

class ArticlesSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField()
    content = serializers.CharField(max_length=300)
    image = serializers.URLField()
    comments = CommentSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(default=True, source='owner.username')
    # author = serializers.ReadOnlyField(source='user.id')
    # = CommentSerializer(many=True, read_only=True)
    # category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())
    # this is a test

    def create(self, validated_data):
        return Articles.objects.create(**validated_data)

class ArticlesDetailSerializer(ArticlesSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        #   instance.author = validated_data.get('author', instance.author)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.content = validated_data.get('content', instance.content)
        #   instance.category = validated_data.get('category',instance.category)
        instance.image = validated_data.get('image', instance.image)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
            


# class CommentSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     message = serializers.CharField(max_length=200)
#     anonymous = serializers.BooleanField()
#     # supporter = serializers.SlugRelatedField(
#     #     slug_field= 'username', 
#     #     queryset= get_user_model().objects.all()
#     # )
#     articles_id = serializers.IntegerField()
#     # message_type = MessageTypeSerializer(many=False, read_only=False)
#     supporter = serializers.ReadOnlyField(source='supporter.id')

#     def create(self, validated_data):
#         return Comment.objects.create(**validated_data)