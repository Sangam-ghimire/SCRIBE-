from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    # my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Book
        fields = [
            'title',
            'content',
            'price',
            'author',
        ]