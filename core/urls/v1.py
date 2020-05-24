from django.conf.urls import url, include
from rest_framework import routers
from autores.views import AuthorViewSet
from books.views import BookViewSet
from editorials.views import EditorialViewSet

router = routers.DefaultRouter()
router.register(r'autores', AuthorViewSet)
router.register(r'editoriales', EditorialViewSet)
router.register(r'libros', BookViewSet)

urlpatterns = [
   url(r'', include(router.urls))
]