from django.contrib import admin
from django.utils.safestring import mark_safe
# from django.utils import mark_safe
# django.utils.html.format_html() 
# Register your models here.
from .models import Place,Image

class ImageInline(admin.TabularInline):

    model = Image

    list_display = ("place","position","preview_image",)

    readonly_fields = ("preview_image",)
    def preview_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.picture.url,
            width="200",
            height="120",
            )
        )

    preview_image.show_discription = "Картинка"



@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title","id",)
    inlines = [ImageInline]




@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ("place","position",)

    # def preview_image(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #         url = obj.picture.url,
    #         width="200",
    #         height="200",
    #         )
    #     )



    

