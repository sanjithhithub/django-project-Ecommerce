# Generated by Django 5.0.2 on 2024-02-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_product_discounted_price_product_discounted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted',
            field=models.BooleanField(),
        ),
    ]
