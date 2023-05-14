from django.http import Http404, JsonResponse

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Book
from .serializers import BooksSerializers

class BookListView(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BooksSerializers(books, many=True)
        return Response(serializer.data)