from django.db import models


class ActiveMixin(models.Model):
    """
    Abstract class to add 'is active' field
    """

    is_active = models.BooleanField(
        db_column    = 'is_active',
        verbose_name = "Is active",
        default      = True,
    )

    class Meta:
        abstract = True
