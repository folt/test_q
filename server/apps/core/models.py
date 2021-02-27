from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey, \
    GenericRelation
from django.contrib.contenttypes.models import ContentType

from django.utils.translation import ugettext_lazy as _


class AbstractDefaultModel(models.Model):
    id = models.BigIntegerField(
        primary_key=True,
        verbose_name=_('id'))

    class Meta:
        abstract = True


class Customers(AbstractUser):
    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')


class OrderStatus(AbstractDefaultModel):
    paid = models.BooleanField(
        verbose_name=_('paid'),
        default=False)

    def __str__(self):
        if self.paid:
            return 'True'
        return 'False'

    class Meta:
        verbose_name = _('order status')
        verbose_name_plural = _('order statuses')


class Emails(AbstractDefaultModel):
    email = models.EmailField(
        verbose_name=_('email'),
        max_length=255)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('email')
        verbose_name_plural = _('emails')


class Products(AbstractDefaultModel):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255)

    price = models.DecimalField(
        verbose_name=_('price'),
        max_digits=6,
        decimal_places=2)

    def __str__(self):
        return f'{self.name} => {self.price}'

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class CustomProducts(AbstractDefaultModel):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255)

    price = models.DecimalField(
        verbose_name=_('price'),
        max_digits=6,
        decimal_places=2)

    def __str__(self):
        return f'{self.name} => {self.price}'

    class Meta:
        verbose_name = _('custom product')
        verbose_name_plural = _('custom products')


class OrderItems(AbstractDefaultModel):
    order = models.ForeignKey(
        'Orders',
        on_delete=models.CASCADE)

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE)

    object_id = models.BigIntegerField(
        db_index=True)

    content_object = GenericForeignKey(
        'content_type',
        'object_id')

    class Meta:
        verbose_name = _('order item')
        verbose_name_plural = _('order items')


class Orders(AbstractDefaultModel):
    number = models.CharField(
        verbose_name=_('name'),
        max_length=255)

    customer = models.ForeignKey(
        'Customers',
        verbose_name=_('customer'),
        on_delete=models.CASCADE)

    order_status = models.ForeignKey(
        'OrderStatus',
        verbose_name=_('order status'),
        on_delete=models.CASCADE)

    email = models.ForeignKey(
        'Emails',
        verbose_name=_('emails'),
        on_delete=models.CASCADE)

    def get_order_items(self):
        return self.orderitems_set.all()

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
