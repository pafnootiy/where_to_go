from django.contrib import admin

# Register your models here.
from .models import Place,Image

class ImageInline(admin.TabularInline):
    model = Image


# class BooksInstanceInline(admin.TabularInline):
#     model = BookInstance

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')
#     inlines = [BooksInstanceInline]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [ImageInline]


    # list_display = (
    #     "title", "image", "pure_phonenumber",'description_short','description_long','latitude',
    #     'longitude',)
# admin.site.register(Place)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ("place","position",)
    

class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [ImageInline]
