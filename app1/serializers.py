from rest_framework import serializers
from .models import *

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedFiles
        fields = '__all__'