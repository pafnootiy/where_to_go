from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(verbose_name="Заголовок",max_length =50)
    image = models.ImageField(upload_to="",verbose_name="Изображение",blank=True)
    description_short=models.TextField(verbose_name="Описание короткое")
    description_long = models.TextField(verbose_name="Описание полное")
    latitude = models.FloatField(verbose_name="Долгота")
    longitude = models.FloatField(verbose_name="Широта")



