# Generated by Django 4.2 on 2024-12-01 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='producttecinfo',
            unique_together={('tec_info', 'tec_info_name')},
        ),
    ]