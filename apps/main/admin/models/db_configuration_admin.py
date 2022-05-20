from django.contrib import admin

from apps.main.admin.forms import DbConfigurationModelForm
from apps.main.admin.mixins import AuditAdminMixin, UpdateOnlyAdminMixin


class DbConfigurationAdmin(AuditAdminMixin, UpdateOnlyAdminMixin, admin.ModelAdmin):

    form = DbConfigurationModelForm
    # list_editable = ('maintenance_mode', 'restrict_frequency_to_TV',)
    search_fields = ('maintenance_mode', 'restrict_frequency_to_TV',)

    def get_list_display(self, request):
        list_display = ('maintenance_mode', 'restrict_frequency_to_TV',) + super(DbConfigurationAdmin, self).get_list_display(request)
        return list_display
