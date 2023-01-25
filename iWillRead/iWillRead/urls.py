from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('section/', include('section_page.urls')),
    path('tinymce/', include('user.urls')),
    path('tinymce/', include('tinymce.urls')),
]
