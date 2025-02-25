# Generated by Django 3.1 on 2023-11-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20231101_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='category',
            field=models.CharField(choices=[('individual', 'Физическое лицо'), ('entity', 'Юридическое лицо')], max_length=20, verbose_name='Категория Контрагента'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Наименование ЮЛ/ФИО ФЛ'),
        ),
    ]
