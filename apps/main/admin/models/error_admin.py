from django.contrib import admin

from apps.main.admin.forms import ErrorModelForm
from apps.main.admin.mixins import AuditAdmin


class ErrorAdmin(AuditAdmin):

    form = ErrorModelForm
    search_fields = ('code', )
    
