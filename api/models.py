from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year_published = models.CharField(max_length=10)
    review = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=180)
    upvotes = models.IntegerField()
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
