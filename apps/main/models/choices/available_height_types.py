from django.db import models
from django.utils.translation import gettext_lazy as _


class AvailableHeightTypes(models.TextChoices):
    AGL   = ('AGL', _('Above Ground Level'))
    AMSL  = ('AMSL', _('Above Mean Sea Level'))
