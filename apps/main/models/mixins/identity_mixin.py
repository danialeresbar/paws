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
 
    def get_id(self):
        return self._id

    def get_uuid(self):
        return self._uuid

    id   = property(get_id, None)
    uuid = property(get_uuid, None)

    class Meta:
        abstract = True

    def __str__(self):
        return f'<{self.__class__.__name__} {self._uuid}>'

    def save(self, *args, **kwargs):
        self.full_clean()
        super(IdentityMixin, self).save(*args, **kwargs)
