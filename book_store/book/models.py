from django.db import models

# Create your models here.

class BookStoreModel(models.Model):
    CATAGORY = (
        ('Mysteri','Mysteri'),
        ('Theriler', 'Theriler'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Humor', 'Humor'),
        ('Horror', 'Horror')
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50, choices=CATAGORY)
    first_pub = models.DateTimeField( auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
    