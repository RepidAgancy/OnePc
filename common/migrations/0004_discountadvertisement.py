# Generated by Django 4.2 on 2024-11-30 13:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_aboutus_description_en_aboutus_description_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountAdvertisement',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='common/discount-advertisement/')),
            ],
            options={
                'verbose_name': 'Discount Adverstisement',
                'verbose_name_plural': 'Discount Advertisements',
            },
        ),
    ]