# Generated by Django 3.1 on 2023-10-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20201014_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='category',
            field=models.CharField(choices=[('individual', 'Физическое лицо'), ('entity', 'Юридическое лицо'), ('', 'Индивидуальный номер налогоплательщика')], max_length=20, verbose_name='Категория'),
        ),
    ]
