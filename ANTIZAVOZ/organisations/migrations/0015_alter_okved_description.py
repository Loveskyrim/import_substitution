# Generated by Django 3.2.13 on 2022-06-12 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0014_okved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='okved',
            name='description',
            field=models.CharField(max_length=2048, verbose_name='Описание'),
        ),
    ]
