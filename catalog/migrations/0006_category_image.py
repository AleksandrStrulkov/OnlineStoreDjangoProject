# Generated by Django 4.2.7 on 2023-11-29 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category/', verbose_name='Изображение'),
        ),
    ]
