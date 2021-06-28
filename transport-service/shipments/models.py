from django.db import models

from locations.models import Location
from drivers.models import Driver


class Shipment(models.Model):
    origin = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='shipment_origin',
    )
    destination = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='shipment_destnation',
    )
    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        related_name='shipment_driver',
    )
    completion = models.DateTimeField()
    created_on = models.DateField(auto_now_add=True)
