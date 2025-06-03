from django.urls import path, include
from rest_framework import  routers
from .views import BookList

router = routers.DefaultRouter()
router.register(r"books", BookList, basename='book')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]