from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    """
    Geneneral purpose Autor Serializer
    """
    class Meta:
        model = Author
        fields = ('name', 'lastname', 'email', 'phone')

