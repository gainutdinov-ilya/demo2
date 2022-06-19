from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"


class Category(models.Model):
    label = models.CharField(
        max_length=128,
        verbose_name='Название'
    )

    def __str__(self):
        return f"{self.label}"


class Order(models.Model):
    max_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Максимальная стоимость'
    )

    photo = models.ImageField(
        verbose_name='Фотография'
    )

    description = models.CharField(
        verbose_name='Описание',
        max_length=512,
    )

    status = models.CharField(
        verbose_name='Статус',
        max_length=12,
        choices=(
            ('new', 'Новый'),
            ('renovating', 'Ремонтируется'),
            ('renovated', 'Отремонтировано')
        ),
        default='new'
    )

    result_image = models.ImageField(
        verbose_name='Конечный результат',
        blank=True
    )

    category = models.ForeignKey(
        verbose_name='Категория',
        to=Category,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        verbose_name='Заказчик',
        to=User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} {self.get_status_display()}"