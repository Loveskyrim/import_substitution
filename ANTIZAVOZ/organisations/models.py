from django.db import models

class organisation(models.Model):
    id_organisation = models.CharField(max_length=200, verbose_name=u"ID организации")
    organisation_name = models.CharField(max_length=200, verbose_name="Имя организации")
    organisation_okved = models.CharField(max_length=8, verbose_name="Вид деятельности", blank=True)
    organisation_category = models.CharField(max_length=8, verbose_name="Категория", blank=True)
    organisation_description = models.CharField(max_length=8, verbose_name="Описание", blank=True)
    organisation_principal = models.CharField(max_length=8, verbose_name="Директор", blank=True)
    organisation_link = models.CharField(max_length=8, verbose_name="Ссылка", blank=True)
    organisation_sanctions = models.CharField(max_length=8, verbose_name="Под санкциями", blank=True)

    def __str__(self):
            return f"{self.pk} {self.id_organisation} {self.organisation_okved} {self.organisation_category} {self.organisation_sanctions}"

    class Meta:
        verbose_name = 'База данных организаций'
        verbose_name_plural = 'Базы данных организаций'
        ordering = ['-id_organisation', '-organisation_okved', '-organisation_category', 
        '-organisation_description', '-organisation_principal', '-organisation_link', '-organisation_sanctions']

class product(models.Model):
    id_product = models.CharField(max_length=200, verbose_name=u"ID продукта")
    product_name = models.CharField(max_length=200, verbose_name="Название продукта")
    product_tags = models.CharField(max_length=8, verbose_name="Тэг", blank=True)
    product_info = models.CharField(max_length=8, verbose_name="Информация о продукте", blank=True)
    product_sanctions_import = models.CharField(max_length=8, verbose_name="Санкции на импорт", blank=True)
    product_sanctions_export = models.CharField(max_length=8, verbose_name="Санкции на экспорт", blank=True)

    def __str__(self):
            return f"{self.pk} {self.product_name} {self.product_tags} {self.product_info} {self.product_sanctions_import} {self.product_sanctions_export}"

    class Meta:
        verbose_name = 'База данных продуктов'
        verbose_name_plural = 'Базы данных продуктов'
        ordering = ['-product_name', '-product_tags', '-product_info', '-product_sanctions_import', '-product_sanctions_export']