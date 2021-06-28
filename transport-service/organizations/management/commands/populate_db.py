import math
from random import randrange

from faker import Faker
from django.utils import timezone
from django_tenants.utils import tenant_context
from django.core.management.base import BaseCommand
from django.db import transaction

from drivers.models import Driver
from shipments.models import Shipment
from locations.models import Location
from organizations.models import Organization


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('required_tenants_num', type=int, nargs='?', default=10)
        parser.add_argument('max_shipping', type=int, nargs='?', default=8)
        parser.add_argument('min_shipping', type=int, nargs='?', default=2)

    @transaction.atomic
    def handle(self, *args, **options):
        max_shipping = options["max_shipping"]
        min_shipping = options["min_shipping"]
        required_tenants_num = options["required_tenants_num"]

        last_tenant_id = 0
        faker = Faker()
        current_tenants_num = Organization.objects.all().count()

        if required_tenants_num <= current_tenants_num:
            return

        if current_tenants_num:
            _, last_tenant_id = Organization.objects.all().order_by(
                'schema_name'
            ).first().schema_name.split('_')
            last_tenant_id = int(last_tenant_id)

        start = last_tenant_id + 1
        end = start + required_tenants_num
        for i in range(start, end):
            tenant = Organization(
                schema_name=f'organization_{i}',
                name=f'Organization {i}',
                paid_until='2016-12-05',
                on_trial=True,
            )
            tenant.save()
            random_shippings_num = randrange(min_shipping, max_shipping)

            with tenant_context(tenant):
                # All commands here are ran under the schema from the
                # `tenant` object.

                # The tenant's locations should double the tenant's shippings.
                for j in range(2 * random_shippings_num):
                    latitude, longitude = faker.latlng()
                    location = Location(
                        name=f'{j}-{i}-{faker.name()}',
                        address=faker.address(),
                        latitude=latitude,
                        longitude=longitude,
                    )
                    location.save()

                location_ids = Location.objects.all().values_list('id', flat=True)
                total = len(location_ids)
                haft = int(math.floor(total / 2))
                origin_ids = location_ids[0:haft]
                destination_ids = location_ids[haft + 1:total]

                # The number of drivers should be the same that the
                # number of shippings.
                for j in range(random_shippings_num):
                    driver = Driver(
                        name=f'{j}-{i}-{faker.name()}',
                    )
                    driver.save()

                driver_ids = Driver.objects.all().values_list('id', flat=True)

                # Create shipments.
                for driver_id, origin_id, destination_id in zip(driver_ids, origin_ids, destination_ids):
                    shipment = Shipment(
                        driver_id=driver_id,
                        origin_id=origin_id,
                        destination_id=destination_id,
                        completion=timezone.now(),
                    )
                    shipment.save()
