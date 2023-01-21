from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
# Register your models here.
from .models import Place,Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title",)


    # list_display = (
    #     "title", "image", "pure_phonenumber",'description_short','description_long','latitude',
    #     'longitude',)
# admin.site.register(Place)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ["place",]
    ordering = ('id',)

