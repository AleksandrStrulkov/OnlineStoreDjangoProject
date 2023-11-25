from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
	name_product = models.CharField(max_length=100, verbose_name='Наименование')
	description_product = models.TextField(verbose_name='Описание', **NULLABLE)
	image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
	category = models.CharField(max_length=100, verbose_name='Категория')
	price = models.IntegerField(verbose_name='Цена')
	created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')

	def __str__(self):
		return f'{self.name_product}{self.description_product}{self.image}{self.category}{self.price}' \
			   f'{self.created_at}{self.updated_at}'

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'


class Category(models.Model):
	name_category = models.CharField(max_length=100, verbose_name='Категория')
	description_category = models.TextField(verbose_name='Описание', **NULLABLE)

	def __str__(self):
		return f'{self.name_category}{self.description_category}'

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
