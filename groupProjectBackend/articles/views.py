from django.shortcuts import render
from rest_framework import status, generics, permissions 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Articles, Comment

from django.http import Http404
from rest_framework import status
from .permissions import  IsOwnerOrReadOnly
from .serializers import (
    CommentSerializer,
    ArticlesDetailSerializer,
    
)

#CategorySerializer add in later


class CommentList(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class ArticlesDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
        
    def get_object(self, pk):
        try:
            # return Articles.objects.get(pk=pk)
            articles = Articles.objects.get(pk=pk)
            self.check_object_permissions(self.request,articles)
            return articles
        except Articles.DoesNotExist:
            raise Http404

        
    def get(self, request, pk):
        articles = self.get_object(pk)
        serializer = ArticlesDetailSerializer(articles)
        return Response(serializer.data)

    def put(self, request, pk):
        articles = self.get_object(pk)
        data = request.data
        serializer = ArticlesDetailSerializer(
            instance=articles,
            data=data,
            partial=True
        )
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)