from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer , CommentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Comment


# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    

class CreateCommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer,
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
            
class CommentDelete(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(author=user)
    
    