from django.db import models

from LiberOasis.utilities import upload_to

# Create your models here.
class Author(models.Model):
    fullname        = models.CharField(max_length=255)
    dob             = models.DateField()
    bio             = models.TextField()
    country         = models.CharField(max_length=128)
    qualification   = models.CharField(max_length=128, blank=True, null=True)
    occupation      = models.CharField(max_length=128, blank=True, null=True)
    photo           = models.ImageField(upload_to=upload_to, null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __repr__(self) -> str:
        return self.fullname