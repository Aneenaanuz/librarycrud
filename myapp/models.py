from django.db import models

class Library(models.Model):
    book_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    author=models.CharField(max_length=150)

    def __str__(self):
        return self.book_name

