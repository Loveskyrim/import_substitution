# Generated by Django 3.2.13 on 2022-06-13 00:31

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('organisations', '0018_auto_20220613_0034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-product_name', '-product_info', '-product_sanctions_import', '-product_sanctions_export'], 'verbose_name': 'База данных продуктов', 'verbose_name_plural': 'Базы данных продуктов'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_tags',
        ),
        migrations.AddField(
            model_name='product',
            name='product_tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]