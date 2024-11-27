from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_year = models.IntegerField()
    rating = models.IntegerField(default=0)  # Add rating field, default to 0

    def __str__(self):
        return self.title
