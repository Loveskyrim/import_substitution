# Generated by Django 3.2.13 on 2022-06-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0015_alter_okved_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='okved',
            name='description',
            field=models.CharField(max_length=10000, verbose_name='Описание'),
        ),
    ]
