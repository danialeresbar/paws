from django.contrib import admin

from apps.main.admin.forms import ErrorModelForm
from apps.main.admin.mixins import AuditAdminMixin


class ErrorAdmin(AuditAdminMixin, admin.ModelAdmin):

    form = ErrorModelForm
    search_fields = ('code', )

    def get_list_display(self, request):
        list_display = ('code',) + super(ErrorAdmin, self).get_list_display(request)
        return list_display
