from django.db import models
from django.contrib.auth.models import User


class Toy(models.Model):
    name = models.CharField(max_length=30, null=True)
    price = models.IntegerField(max_length=10, null=True)
    dicription = models.CharField(max_length=255, null=True)
    # image = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", null=True)

    class Meta:
        managed = False
        db_table = 'toys'


# class Users(models.Model):
#     user_name = models.CharField(max_length=50, verbose_name="Имя пользователя")
#     login = models.CharField(max_length=50, verbose_name="Логин")
#     password = models.CharField(max_length=50, verbose_name="Пароль")
#
#     class Meta:
#         managed = False
#         db_table = 'users'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    toy = models.ForeignKey(Toy, on_delete = models.CASCADE)
    amount = models.IntegerField(verbose_name='Количество', default=1)

    class Meta:
        managed = True
        db_table = 'basket'