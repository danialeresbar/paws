from apps.main.models import (
    Error
)

from paws.admin import admin_site
from .models import (
    ErrorAdmin
)

admin_site.register(Error, ErrorAdmin)
