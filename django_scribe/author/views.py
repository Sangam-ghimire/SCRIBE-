from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Author
from .serializer import AuthorSerializer
# Create your views here.

class AuthorAPI(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        
        print(serializer.data)
        return Response(serializer.data)
