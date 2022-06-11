from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class organisation(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('registered', 'Registered'),
    )
    id_organisation = models.CharField(max_length=200, verbose_name=u"ID организации")
    organisation_name = models.CharField(max_length=200, verbose_name=u"Имя организации")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'Пользователь регистратор', default=1)
    slug = models.SlugField(max_length=250, unique_for_date='publish', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    organisation_okved = models.CharField(max_length=8, verbose_name=u"Вид деятельности", blank=True)
    organisation_category = models.CharField(max_length=8, verbose_name=u"Категория", blank=True)
    organisation_description = models.TextField(verbose_name=u"Описание", blank=True)
    organisation_principal = models.CharField(max_length=8, verbose_name=u"Директор", blank=True)
    organisation_link = models.CharField(max_length=8, verbose_name=u"Ссылка", blank=True)
    organisation_sanctions = models.CharField(max_length=8, verbose_name=u"Под санкциями", blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return f"{self.pk} {self.id_organisation} {self.organisation_okved} {self.organisation_category} {self.organisation_sanctions}"

    class Meta:
        verbose_name = 'База данных организаций'
        verbose_name_plural = 'Базы данных организаций'
        ordering = ['-id_organisation', '-organisation_okved', '-organisation_category',
                    '-organisation_description', '-organisation_principal', '-organisation_link',
                    '-organisation_sanctions']


class product(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('registered', 'Registered'),
    )
    id_product = models.CharField(max_length=200, verbose_name=u"ID продукта")
    product_name = models.CharField(max_length=200, verbose_name=u"Название продукта")
    author = models.ForeignKey(organisation, on_delete=models.CASCADE, verbose_name=u'Организация владелец')
    slug = models.SlugField(max_length=250, unique_for_date='publish', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    product_tags = models.CharField(max_length=8, verbose_name=u"Тэг", blank=True)
    product_info = models.TextField(verbose_name=u"Информация о продукте", blank=True)
    product_sanctions_import = models.CharField(max_length=8, verbose_name=u"Санкции на импорт", blank=True)
    product_sanctions_export = models.CharField(max_length=8, verbose_name=u"Санкции на экспорт", blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return f"{self.pk} {self.product_name} {self.product_tags} {self.product_info} {self.product_sanctions_import} {self.product_sanctions_export}"

    class Meta:
        verbose_name = 'База данных продуктов'
        verbose_name_plural = 'Базы данных продуктов'
        ordering = ['-product_name', '-product_tags', '-product_info', '-product_sanctions_import',
                    '-product_sanctions_export']
