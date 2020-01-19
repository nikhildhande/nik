from rest_framework.serializers import ModelSerializer
from bookstore.models import *


class BookSerialier(ModelSerializer):
    class Meta:
        model =Book
        fields = '__all__'


class AuthorSerialier(ModelSerializer):
    class Meta:
        model =Author
        fields = '__all__'


class PublisherSerialier(ModelSerializer):
    class Meta:
        model =Publisher
        fields = '__all__'


class AddressSerialier(ModelSerializer):
    class Meta:
        model =Address
        fields = '__all__'