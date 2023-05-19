from django.db import models

class Book(models.Model):
    book_Id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} : {self.book_Id}'
    
    

    

