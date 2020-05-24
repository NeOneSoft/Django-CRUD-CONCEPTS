from rest_framework import serializers

from autores.serializers import AuthorSerializer
from editorials.serializers import EditorialSerializer
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    General pourpose Book serializer
    """
    authors = AuthorSerializer(many=True, read_only=True)
    editorial = EditorialSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('title', 'authors', 'editorial', 'date_pub')


class CreateBookSerializer(serializers.ModelSerializer):
    """
    Create Book Serializer without related fields
    """

    class Meta:
        model = Book
        fields = ('title', 'authors', 'editorial', 'date_pub')
