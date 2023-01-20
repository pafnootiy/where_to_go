from django.contrib import admin

# Register your models here.
from .models import Place
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "title",)
    # list_display = (
    #     "title", "image", "pure_phonenumber",'description_short','description_long','latitude',
    #     'longitude',)
# admin.site.register(Place)