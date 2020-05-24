from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from autores.models import Author
from autores.serializers import AuthorSerializer
from books.models import Book
from books.serializers import BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    Author endpoint(ViewSet)
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True, methods=['GET'])
    def libros(self, request, pk=None):
        autor = self.get_object()
        libros = Book.objects.filter(authors__id=autor.id)
        serialized = BookSerializer(libros, many=True)
        if not libros:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este autor no tiene libros'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)
