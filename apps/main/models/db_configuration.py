from django.db import models
from django.utils.translation import gettext as _

from .mixins import AuditMixin, IdentityMixin


class DbConfiguration(AuditMixin, IdentityMixin):
    """

    """

    maintenance_mode = models.BooleanField(
        db_column='maintenance_mode',
        verbose_name=_('Maintenance mode'),
        default=False
    )
    restrict_frequency_to_TV = models.BooleanField(
        db_column='restrict_frequency_to_TV',
        verbose_name=_('Restrict to TV frequency'),
        default=True
    )
    # backup_list = models.ForeignKey(
    #     'paws.DbUpdateSpec',
    #     db_column='backup_list',
    #     verbose_name=_('Default DbUpdateSpec list'),
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL
    # )

    class Meta:
        verbose_name = 'DB Configuration'
        verbose_name_plural = 'DB Configurations'
        db_table = 'db_configurations'

    def __str__(self):
        return _('Edit database configuration')
