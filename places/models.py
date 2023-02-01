from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name="Заголовок",max_length =50)
    short_description=HTMLField(verbose_name="Описание короткое",null=True)
    long_description = HTMLField(verbose_name="Описание полное",null=True)
    longitude = models.FloatField(verbose_name="Долгота")
    latitude = models.FloatField(verbose_name="Широта")
    
    def __str__(self) :
        
        return self.title

class Image(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE,verbose_name='Локация',
                              related_name='images',blank=True,null=True)
    picture = models.ImageField(verbose_name="Изображение",blank=True,null=True)
    position =models.PositiveIntegerField(unique=False,blank=True,null=True,verbose_name="Номер",default=0)
    
    class Meta:
        ordering = ["position"]
