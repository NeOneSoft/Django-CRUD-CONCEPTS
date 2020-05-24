"""Musica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
#Para el versionado redefinimos nuestras urls en
#nuestra app core, desaparecen de aqui


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#Obtiene token
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #Refresca el token
    path('api/v1/', include('core.urls.v1')),#Definomos dedonde se toman las urls para la v1
    path('admin/', admin.site.urls),
    path('documentation', include_docs_urls(title='Biblioteca API', public=True))
]

"""
Recordar

En caso de que no exista versionado el codigo es el siguiente:
Lo que importamos es:

from django.conf.urls import url, include
from rest_framework import routers
from autores.views import AuthorViewSet
from books.views import BookViewSet
from editorials.views import EditorialViewSet

Y los urlspatterns son:

urlpatterns = [
   path('', include(router.urls)),
   path('admin/', admin.site.urls),
]
"""