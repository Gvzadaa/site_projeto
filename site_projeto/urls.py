from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja.urls')),  # Inclui TODAS as rotas do app loja
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)