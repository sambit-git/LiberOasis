from datetime import date
import os

from django.db import models

from authors.models import Author
from LiberOasis.utilities import upload_to

# Create your models here.
class Book(models.Model):
    title           = models.CharField(max_length=255)
    description     = models.TextField()
    authors         = models.ManyToManyField(Author)
    price           = models.DecimalField(max_digits=5, decimal_places=2)
    publication     = models.CharField(max_length=255, null=True, blank=True)
    issue_duration  = models.IntegerField(default=30)
    publish_year    = models.IntegerField(default=date.today().year)
    book_cover      = models.ImageField(upload_to=upload_to, null=True, blank=True)
    pdf             = models.FileField(upload_to=upload_to, null=True, blank=True)
    stock           = models.IntegerField(default=10)
    active          = models.BooleanField(default=True)
    featured        = models.BooleanField(default=False)
    @property
    def fine(self):
        return 2*self.price
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __repr__(self) -> str:
        return self.title