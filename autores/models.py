from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email =  models.CharField(max_length=100)
    phone = models.CharField(max_length=200)

    def __str__(self):   #Retorna el nombre de este modelo
        return self.name
