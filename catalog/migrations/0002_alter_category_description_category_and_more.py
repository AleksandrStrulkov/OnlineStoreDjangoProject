# Generated by Django 4.2.7 on 2023-11-25 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description_category',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_product',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
