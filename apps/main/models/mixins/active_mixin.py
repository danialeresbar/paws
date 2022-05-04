from django.db import models


class ActiveMixin(models.Model):
    """
    Abstract class to add 'is active' field
    """

    _is_active = models.BooleanField(
        db_column    = 'is_active',
        verbose_name = "Is active",
        default      = True,
    )

    def get_is_active(self):
        return self._is_active

    def set_is_active(self, value):
        self._is_active = value

    is_active = property(get_is_active, set_is_active)

    class Meta:
        abstract = True
