from rest_framework import serializers

from .models import Book
from authors.models import Author

class BooksSerializers(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Book
        fields = [
            "title",
            "description",
            "authors",
            "price",
            "publication",
            "issue_duration",
            "publish_year",
            "book_cover",
            "pdf",
            "stock",
                  ]
    def get_authors(self, instance):
        authors = []
        for author in instance.authors.all():
            authors.append(author.fullname)
        return authors
    