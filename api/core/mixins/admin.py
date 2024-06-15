from django.contrib import admin


class BaseAdminCreatedMixin(admin.ModelAdmin):
    exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, "created_by") and request.user:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
