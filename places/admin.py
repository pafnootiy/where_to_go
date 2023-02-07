from adminsortable2.admin import SortableAdminBase
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableTabularInline
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    extra = 1
    list_display = ('preview_image', 'place', 'position',)

    readonly_fields = ('preview_image',)

    def preview_image(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.picture.url,
                width='200',
                height='120',
            )
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('position', 'place',)
