from django.contrib.gis import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from server.apps.core import models as core_models


class CustomersAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
    ]


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'paid',
    ]
    list_filter = [
        'paid'
    ]


class EmailsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
    ]


class ProductsAdmin(admin.OSMGeoAdmin):
    list_display = [
        'id',
        'name',
        'price',
    ]


class CustomProductsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'price',
    ]


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'content_type',
        'object_id',
        'content_object',
    ]


class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'number',
        'customer',
        'order_status',
        'email',
    ]
    raw_id_fields = [
        'customer',
        'order_status',
        'email',
    ]


admin.site.register(core_models.Customers, CustomersAdmin)
admin.site.register(core_models.OrderStatus, OrderStatusAdmin)
admin.site.register(core_models.Emails, EmailsAdmin)
admin.site.register(core_models.Products, ProductsAdmin)
admin.site.register(core_models.CustomProducts, ProductsAdmin)
admin.site.register(core_models.OrderItems, OrderItemsAdmin)
admin.site.register(core_models.Orders, OrdersAdmin)
