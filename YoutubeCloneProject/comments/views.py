from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CommentList(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400__BAD_REQUEST)


class Detail(APIView):

    def get_comments(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response (status = 404)

    def get(self, request, pk):
        comments = self.get_comments(pk=pk)
        serializer = CommentSerializer(comments)
        return Response(serializer.data)

    def put(self, request, pk):
        comments = self.get_comments(pk=pk)
        serializer = CommentSerializer(comments, data=request.data)
        if  serializer.is_valid():    
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
            comments = self.get_comments(pk=pk)
            comments.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
