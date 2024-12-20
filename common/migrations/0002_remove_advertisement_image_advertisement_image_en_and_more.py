# Generated by Django 4.2 on 2024-12-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='image',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='image_en',
            field=models.ImageField(null=True, upload_to='media/common/advertisement'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='media/common/advertisement'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='image_uz',
            field=models.ImageField(null=True, upload_to='media/common/advertisement'),
        ),
    ]
