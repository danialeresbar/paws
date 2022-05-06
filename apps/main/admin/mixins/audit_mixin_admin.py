from django.contrib import admin


class AuditAdmin(admin.ModelAdmin):

    list_display = ('_created_at', '_updated_at')
    list_filter = ('_created_at', '_updated_at')

