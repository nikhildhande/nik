
from django.db import models


# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active='Y')


# Book(id=7771,name='Python',price=273.45,cat='A')

class Book(models.Model):
    name = models.CharField('bk_name', max_length=100)
    price = models.FloatField()
    cat = models.CharField(max_length=10)
    active = models.CharField(max_length=10, default='Y')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='bookref', null=True)
    all_books = models.Manager()
    active_books = ActiveManager()


# Publisher(id=99991,name='TTT',reviews='xstars')
class Publisher(models.Model):
    name = models.CharField('bk_name', max_length=100)
    reviews = models.CharField(max_length=10)
    active = models.CharField(max_length=10, default='Y')
    all_publishers = models.Manager()
    active_publishers = ActiveManager()


# Author(id=1112,name='XXX',balance=2383.45)
class Author(models.Model):
    name = models.CharField('bk_name', max_length=100)
    balance = models.FloatField()
    active = models.CharField(max_length=10, default='Y')
    books = models.ManyToManyField(Book)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='authorref', null=True)
    all_authors = models.Manager()
    active_authors = ActiveManager()


# Address(id=101,city='Pune',pincode=283834)
class Address(models.Model):
    city = models.CharField('bk_name', max_length=100)
    pincode = models.IntegerField()
    state = models.CharField(max_length=100)
    active = models.CharField(max_length=10, default='Y')
    publisher = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='addressref', null=True)
    all_addresses = models.Manager()
    active_addresses = ActiveManager()


'''
Book
    author -- MM
    PUBLISHER -- M-1
    ADDRESS -- NA

publisher 
    author -- na
    address -- 11
    book  -- 1-m

author
    book -- mm
    address -- m-1
    publisher -- na

address
    pubshlisher -- 11
    author -- 1-m



'''