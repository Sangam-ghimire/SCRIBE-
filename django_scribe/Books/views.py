from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Book
from .serializer import BookSerializer
# Create your views here.

class AllBooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        
        print(serializer.data)
        return Response(serializer.data)
