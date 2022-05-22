from rest_framework import serializers
from .models import Articles, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class ArticlesSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField()
    content = serializers.CharField(max_length=300)
    image = serializers.URLField()
    # author = serializers.ReadOnlyField(source='user.id')
    # comment = CommentSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())
    # this is a test

    def create(self, validated_data):
        return Articles.objects.create(**validated_data)

class ArticlesDetailSerializer(ArticlesSerializer):
    # comment = CommentSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
          instance.title = validated_data.get('title', instance.title)
        #   instance.author = validated_data.get('author', instance.author)
          instance.pub_date = validated_data.get('pub_date', instance.pub_date)
          instance.content = validated_data.get('content', instance.content)
          instance.category = validated_data.get('category',instance.category)
          instance.image = validated_data.get('image', instance.image)
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