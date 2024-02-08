from django.db import models
from django.urls import reverse
# Create your models here.

# При реализации дополнительных опций
# class Category(models.Model):
#     """
#     Модель, описывающая услуги, оказываемые на сайте
#     """
#     title = models.CharField(max_length=150, unique=True, verbose_name='Название')
#     slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
#     description = models.TextField(blank=True, null=True, verbose_name='Описание категории')
#     image = models.ImageField(upload_to='category_images', blank=True, null=True, verbose_name='Изображение')

#     class Meta:
#         db_table = 'category'
#         verbose_name = 'Категорию'
#         verbose_name_plural = 'Категории'

#     def __str__(self):
#         return self.title

class Route(models.Model):
    """
    Модель существующих маршрутов
    """
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание маршрута')
    complexity = models.DecimalField(default=5.00, max_digits=3, decimal_places=2, verbose_name="Сложность" ) # Возможно переделать, чтобы не проводить доп.действий
    duration = models.PositiveSmallIntegerField(verbose_name='Продолжительность')
    distance = models.CharField(max_length=50, verbose_name='Протяженность')
    image = models.ImageField(upload_to='category_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, verbose_name='Цена маршрута')
    # category = models.ForeignKey(to=Category, on_delete=models.SET_DEFAULT, verbose_name='Категория')

    class Meta:
        db_table = 'route'
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ('id', )
    
    
    def __str__(self):
        return f'{self.name} - {self.price}'
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"route_slug": self.slug})
    
