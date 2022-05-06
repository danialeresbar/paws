from django.db import models
from django.utils.translation import gettext as _

from .device_descriptor import DeviceDescriptor
from .mixins import AuditMixin, IdentityMixin


class DeviceValidity(AuditMixin, IdentityMixin):
    """

    """

    is_valid = models.BooleanField(
        verbose_name=_('Is valid?'),
        default=True
    )
    reason = models.CharField(
        verbose_name=_('Reason'),
        max_length=128
    )
    descriptor = models.ForeignKey(
        DeviceDescriptor,
        verbose_name=_('Descriptor'),
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Device Validity'
        verbose_name_plural = 'Device Validity'
        db_table = 'device validity'
        managed = False
