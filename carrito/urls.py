"""carrito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Para configurar la carga de ficheros media, hay que detectar la configuracion, por lo que importamos
from django.conf import settings
# Importamos la tupla de url pages de esta manera
from publications.urls import publications_patterns
from wish_list.urls import wish_list_patterns
from shopping_basket.urls import shopping_basket_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('core.urls')),
    path('', include(publications_patterns)),
    path('wish_lists/', include(wish_list_patterns)),
    path('shopping_basket_lists/', include(shopping_basket_patterns)),


    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]


admin.site.site_header = settings.ADMIN_SITE_HEADER

# Comprobar si estamos en debug
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)