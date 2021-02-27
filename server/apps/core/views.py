from django.views.generic import ListView
from server.apps.core import models as core_models


class TestView(ListView):
    template_name = 'test.html'
    queryset = core_models.Orders.objects\
        .select_related('customer', 'order_status', 'email')\
        .prefetch_related('orderitems_set__content_object')\
        .all()
