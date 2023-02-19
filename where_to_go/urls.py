
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


from where_to_go import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path(
        'places/<int:pk>/', views.add_information_for_location,
        name='location_info'
    ),
    path('tinymce/', include('tinymce.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
