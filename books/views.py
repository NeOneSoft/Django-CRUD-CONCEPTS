from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from autores.models import Author
from autores.serializers import AuthorSerializer
from books.models import Book
from books.serializers import BookSerializer, CreateBookSerializer
from editorials.models import Editorial
from editorials.serializers import EditorialSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa una instancia de un libro de acuerdo al ID mandado.
    list:
        Regresa la lista de libros en la base de datos.
    create:
        Crea un libro en la base de datos.
    delete:
        Elimina un libro.
    update:
        Actualiza un libro.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    #Sobre escibimos nuestra clase get_serializaer
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateBookSerializer
        return BookSerializer



    # Forma alternativa de traer autores
    @action(detail=True, methods=['GET'])
    def autores(self, request, pk=None): # Este es el nombre que hay que poner en la url: http://127.0.0.1:8000/libros/1/autores/
        book = self.get_object()
        autores = book.authors.all()
        serialized = AuthorSerializer(autores, many=True)
        if not autores:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este libro no tiene autores'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    # Forma alternativa de traer editoriales
    @action(detail=True, methods=['GET'])
    def editoriales(self, request, pk=None): # Este es el nombre que hay que poner en la url: http://127.0.0.1:8000/libros/1/editoriales/
        book = self.get_object()
        editorial = book.editorial
        serialized = EditorialSerializer(editorial)
        if not editorial:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este libro no tiene autores'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=False, methods=['GET'])
    def recent(self, request):
        books = Book.objects.all().order_by('-date_pub')
        serialized = BookSerializer(books, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)


    """
    @action(detail=True, methods=['GET'])
    def editoriales(self, request, pk=None):
        book = self.get_object()
        editoriales = Editorial.objects.filter(book__id=book.id)
        serialized = EditorialSerializer(editoriales, many=True)
        if not editoriales:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este libro no tiene editoriales'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)

        # Forma alternativa de traer autores
        @action(detail=True, methods=['GET'])
        def autores(self, request, pk=None):
            book = self.get_object()
            autores = book.authors.all()
            serialized = AuthorSerializer(autores, many=True)
            if not autores:
                return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este libro no tiene autores'})
            return Response(status=status.HTTP_200_OK, data=serialized.data)
    """