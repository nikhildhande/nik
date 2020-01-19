# Create your views here.
from django.shortcuts import render
from bookstore.models import *
from bookstore.serializers import *
from rest_framework.viewsets import *


class BookOperations(ModelViewSet):
    queryset = Book.active_books.all()
    serializer_class = BookSerialier


class AuthorOperations(ModelViewSet):
    queryset = Author.active_authors.all()
    serializer_class = AuthorSerialier


class AddressOperations(ModelViewSet):
    queryset = Address.active_addresses.all()
    serializer_class = AddressSerialier


class PublisherOperations(ModelViewSet):
    queryset = Publisher.active_publishers.all()
    serializer_class = PublisherSerialier