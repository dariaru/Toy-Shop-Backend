from stocks.models import Toy, Basket, User
from rest_framework import serializers


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ["pk", "name", "price", "dicription", "image"]


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = User
        # Поля, которые мы сериализуем
        fields = ["pk", "username", "password", 'is_staff']


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Basket
        # Поля, которые мы сериализуем
        fields = ["pk", "user", "toy", "amount"]
