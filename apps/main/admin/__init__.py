from apps.main.admin.models import (
    DbConfigurationAdmin,
    ErrorAdmin
)
from apps.main.models import (
    DbConfiguration,
    Error
)

from paws.admin import admin_site


admin_site.register(DbConfiguration, DbConfigurationAdmin)
admin_site.register(Error, ErrorAdmin)
