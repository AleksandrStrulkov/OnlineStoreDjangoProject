from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
	name_product = models.CharField(max_length=100, verbose_name='Наименование')
	description_product = models.TextField(verbose_name='Описание')
	image = models.ImageField(upload_to='products/', verbose_name='Изображение')
	category = models.CharField(max_length=100, verbose_name='Категория')
	price = models.IntegerField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
	name_category = models.CharField(max_length=100, verbose_name='Категория')
	description_category = models.TextField('Описание')

