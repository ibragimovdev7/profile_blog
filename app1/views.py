from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets

class AutorView(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class FileView(viewsets.ModelViewSet):
    queryset = LinkedFiles.objects.all()
    serializer_class = FileSerializer   
