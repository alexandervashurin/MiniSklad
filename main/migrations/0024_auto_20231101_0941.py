# Generated by Django 3.1 on 2023-11-01 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20231101_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='inn',
            field=models.CharField(max_length=12, unique=True, verbose_name='ИНН'),
        ),
    ]
