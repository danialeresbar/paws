import uuid

from django.db import models


class IdentityMixin(models.Model):
    """
    Base mixin to add identifiers
    """

    _id = models.AutoField(
        db_column    = 'id',
        auto_created = True,
        primary_key  = True,
        serialize    = False,
        verbose_name = 'ID'
    )

    _uuid = models.UUIDField(
        db_column = 'uuid',
        unique    = True,
        default   = uuid.uuid4,
        editable  = False
    )

    @property
    def id(self):
        return self._id

    @property
    def uuid(self):
        return self._uuid

    class Meta:
        abstract = True

    def __str__(self):
        return f'<{self.__class__.__name__} {self._uuid}>'
