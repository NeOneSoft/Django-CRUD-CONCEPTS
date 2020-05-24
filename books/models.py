from django.db import models
from django.utils import timezone

from autores.models import Author
from editorials.models import Editorial

from django.forms import ModelForm


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)  # unique=True Para no repetir un valor en el campo(Primera Opcion)
    authors = models.ManyToManyField(Author)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    date_pub = models.DateField('Fechas de publicacion', default=timezone.now())

    def __str__(self):
        return self.title


class Meta:  # Esto es para que la prueba salga sin warning
    ordering = ('-date_pub',)


#FORMS FROM THE MODELS
"""
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['authors', 'editorial', 'date_pub']
"""

#FUNCTION TO NON REPEATED TITLE BOOKS
"""
Uncomment to check the function
    #Declaramos una funcion para no repetir el mismo libro (Segunda Opcion)
    def save(self, *args, **kwargs):
        book = Book.objects.filter(title=self.title)
        if not book.exist():
            book.save()
        else:
            pass
        super(Book, self).save(*args, **kwargs)
"""
