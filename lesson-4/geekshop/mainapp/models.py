from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='Имя категории',
    )
    description = models.DateTimeField(
        verbose_name='Описание',
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Availability(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='Имя категории',
    )

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name='Категория',
    )
    name = models.CharField(
        verbose_name='Имя продукта',
        max_length=128,
    )
    image = models.ImageField(
        upload_to='products_img',
        blank=True,
    )

    short_desc = models.CharField(
        max_length=256,
        verbose_name='краткое описание',
        blank=True,
    )

    description = models.TextField(
        verbose_name='описание продукта',
        blank=True,
        max_length=500
    )

    price = models.DecimalField(
        verbose_name='цена продукта',
        max_digits=8,
        decimal_places=2,
        default=0,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0
    )
    manufacture = models.CharField(
        verbose_name='Проиводитель',
        max_length=128,
    )
    model = models.CharField(
        verbose_name='Наименование модели',
        max_length=64,
    )
    availability = models.ForeignKey(
        Availability,
        on_delete=models.CASCADE,
        verbose_name='Доступность',
    )

    def __str__(self):
        return f'{self.name} ({self.category.name}) | {self.model}'

