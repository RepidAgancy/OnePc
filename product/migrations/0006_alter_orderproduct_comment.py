# Generated by Django 4.2 on 2024-12-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_orderproduct_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]