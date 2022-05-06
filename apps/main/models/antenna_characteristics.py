from django.db import models
from django.utils.translation import gettext as _

from .choices import AvailableHeightTypes
from .mixins import AuditMixin, IdentityMixin


class AntennaCharacteristics(AuditMixin, IdentityMixin):
    """

    """

    height = models.FloatField(
        verbose_name=_('Height'),
        null=True,
        blank=True
    )
    height_type = models.CharField(
        verbose_name=_('Height type'),
        choices=AvailableHeightTypes.choices,
        max_length=10,
        null=True,
        blank=True,
        default=AvailableHeightTypes.AGL
    )
    height_uncertainty = models.FloatField(
        verbose_name=_('Height uncertainty'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Antenna Characteristics'
        verbose_name_plural = 'Antenna Characteristics'
        db_table = 'antenna_characteristics'
        managed = False

    def __str__(self):
        return '{} - {}'.format(self.height_type, self.height)
