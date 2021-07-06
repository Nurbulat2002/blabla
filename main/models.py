from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from asd.utils import autoslug


class TimeABC(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data sozdaniya')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Data sozdaniya')

    class Meta:
        abstract = True


@autoslug('title')
class Product(TimeABC):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100, verbose_name='Nazvanie tovara')
    des = models.TextField(verbose_name='Opicanie tovara')
    count_bill = models.PositiveIntegerField(default=0, verbose_name='kol-vo')

    class Meta:
        verbose_name = 'Tovar'
        verbose_name_plural = 'Tovary'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Kartinki tovarov')


class Bill(TimeABC):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bill')
    quantity = models.PositiveIntegerField(default=0)


@receiver(post_save, sender=Bill)
def count(sender, instance, *args, **kwargs):
    count_bill = getattr(instance.product, 'count_bill')
    q = instance.quantity
    count_bill += q
    setattr(instance.product, 'count_bill', count_bill)
    instance.product.save()
