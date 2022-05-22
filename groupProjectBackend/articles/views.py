from django.shortcuts import render
from rest_framework import status, generics, permissions 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Articles, Category 
from django.http import Http404
from rest_framework import status
from .permissions import  IsOwnerOrReadOnly
from .serializers import ArticlesSerializer, ArticlesDetailSerializer, CategorySerializer, CategoryDetailSerializer


class ArticlesList(APIView):
    permission_classes = [
            permissions.IsAuthenticatedOrReadOnly, 
            IsOwnerOrReadOnly
        ]

    def get(self, request):
        articles = Articles.objects.all()
        
        order_by = request.query_params.get('order_by', None)
        if order_by:
            articles = articles.order_by(order_by)

        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

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

    def delete(self, request, pk):
        articles = self.get_object(pk)
        articles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#CategorySerializer 
class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetail(APIView):
    
    def get_object(self, **kwargs):
        try:
            if "slug" in kwargs:
                return Category.objects.get(slug=kwargs["slug"])
            return Category.objects.get(pk=kwargs["pk"])
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, **kwargs):
        category = self.get_object(**kwargs)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

# class CommentList(APIView):

#     def get(self, request):
#         comments = Comment.objects.all()
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)
        
#     def post(self, request):
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(supporter=request.user)
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#                 )
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)