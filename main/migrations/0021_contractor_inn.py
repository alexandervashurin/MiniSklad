# Generated by Django 3.1 on 2023-11-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20231019_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='inn',
            field=models.CharField(default='', max_length=12),
        ),
    ]
