from django.contrib import admin

from apps.main.admin.forms import AntennaCharacteristicsModelForm
from apps.main.admin.mixins import AuditAdminMixin


class AntennaCharacteristicsAdmin(AuditAdminMixin, admin.ModelAdmin):

    form = AntennaCharacteristicsModelForm
    search_fields = ('code', )

    def get_list_display(self, request):
        list_display = ('height_type', 'height') + super(AntennaCharacteristicsAdmin, self).get_list_display(request)
        return list_display
