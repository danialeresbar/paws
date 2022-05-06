from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _

from .mixins import AuditMixin


class Error(AuditMixin):
    """

    """

    code = models.IntegerField(
        verbose_name=_('Code'),
        validators=[MinValueValidator(-32768), MaxValueValidator(32767)],
        primary_key=True
    )
    message = models.CharField(
        verbose_name=_('Message'),
        max_length=128,
        blank=True,
        default=''
    )
    data = models.JSONField(
        verbose_name=_('Data'),
        null=True,
        blank=True,
        default=dict,
    )

    class Meta:
        verbose_name = 'Error'
        verbose_name_plural = 'Errors'
        db_table = 'errors'

    def __str__(self):
        return f'Error code: {self.code}'
