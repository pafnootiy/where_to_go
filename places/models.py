from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(verbose_name="Заголовок",max_length =50)
    # image = models.ImageField(upload_to="",verbose_name="Изображение",blank=True)
    description_short=models.TextField(verbose_name="Описание короткое")
    description_long = models.TextField(verbose_name="Описание полное")
    latitude = models.FloatField(verbose_name="Долгота")
    longitude = models.FloatField(verbose_name="Широта")

    def __str__(self) :
        return self.title

class Image(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE,verbose_name='Локация',
                              related_name='images',blank=True,null=True)
    picture = models.ImageField(upload_to="media",verbose_name="Изображение",blank=True)
    position =models.PositiveIntegerField(unique=True,blank=True,null=True,verbose_name="Номер")

    # def __str__(self) :
    #     return self.place




