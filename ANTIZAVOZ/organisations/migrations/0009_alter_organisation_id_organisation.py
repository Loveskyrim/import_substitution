# Generated by Django 3.2.13 on 2022-06-11 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0008_alter_organisation_organisation_inn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='id_organisation',
            field=models.CharField(blank=True, max_length=200, verbose_name='ID организации'),
        ),
    ]
