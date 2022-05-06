from django.db import models
from django.utils.translation import gettext as _

from .mixins import AuditMixin, IdentityMixin


class DeviceDescriptor(AuditMixin, IdentityMixin):
    """

    """

    serial_number = models.CharField(
        verbose_name=_('Serial number'),
        max_length=64,
        null=True,
        blank=True,
    )
    manufacturer_id = models.CharField(
        verbose_name=_('Manufacturer Id'),
        max_length=64,
        null=True,
        blank=True,
    )
    model_id = models.CharField(
        verbose_name=_('Model Id'),
        max_length=64,
        null=True,
        blank=True
    )
    # rulesets = models.ManyToManyField(
    #     'paws.RulesetInfo',
    #     verbose_name=_('Supported rulesets'),
    #     blank=True
    # )
    other = models.JSONField(
        verbose_name=_('Other'),
        null=True,
        blank=True,
        default=dict
    )

    class Meta:
        verbose_name = 'Device Descriptor'
        verbose_name_plural = 'Device Descriptors'
        db_table = 'device_descriptors'
        managed = False

    def __str__(self):
        return 'Descriptor {}'.format(self.uuid)
