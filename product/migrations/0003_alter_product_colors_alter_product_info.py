# Generated by Django 4.2 on 2024-12-14 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_orderproduct_user_discountproduct_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='product.productcolor'),
        ),
        migrations.AlterField(
            model_name='product',
            name='info',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='product.producttecinfo'),
        ),
    ]
