class UpdateOnlyAdminMixin:

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
