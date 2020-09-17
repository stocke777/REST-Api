from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):   # using ModelSerializer attached to certain Model
    class Meta:
        model = Article
        fields = ['id', 'author', 'email']

# class ArticleSerializer(serializers.Serializer):          # how the serializer is written manually
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#     date = serializers.DateTimeField()

#     def create(self, validated_data):                     # to create and article object with data
#         return Article.objects.create(validated_data)
    
#     def update(self, instance, validated_data):              # to update the certain instance if data is valid
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance