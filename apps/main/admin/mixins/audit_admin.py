class AuditAdminMixin:
    """
    Mixin Data that modifies the fields that are displayed
    """

    list_display = ('_created_at', '_updated_at')

