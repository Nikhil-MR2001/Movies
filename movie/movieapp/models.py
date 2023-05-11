from django.db import models


# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=111)
    year = models.IntegerField()
    image = models.ImageField(upload_to='media')
    description = models.CharField(max_length=500, default='No description available')


    def __str__(self):
        return self.name
