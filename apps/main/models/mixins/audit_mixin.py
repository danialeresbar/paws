from django.db import models


class AuditMixin(models.Model):
    """
    Abstract class used if a model should be audited
    """

    _created_at = models.DateTimeField(
        db_column    = 'created_at',
        verbose_name = 'Creation date',
        auto_now_add = True
    )

    _updated_at = models.DateTimeField( 
        db_column    = 'updated_at',
        verbose_name = 'Last update date',
        auto_now     = True
    )

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    class Meta:
        abstract = True
