from django.db import models

class Editorial(models.Model):
    name_ed = models.CharField(max_length=100)
    direction = models.CharField(max_length=100)
    web_page = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name_ed
