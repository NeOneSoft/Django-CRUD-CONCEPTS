from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer
from editorials.models import Editorial
from editorials.serializers import EditorialSerializer


class EditorialViewSet(viewsets.ModelViewSet):
    """
    Editorial (EndPoint)
    """
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    @action(detail=True, methods=['GET'])
    def libros(self, request, pk=None):
        editorial = self.get_object()
        libros = Book.objects.filter(editorial__id=editorial.id)
        serialized = BookSerializer(libros, many=True)
        if not libros:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Esta editorial no tiene libros'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)