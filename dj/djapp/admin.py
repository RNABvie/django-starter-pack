from django.contrib import admin
from djapp import models


#########################################

admin.site.register(models.Room)
admin.site.register(models.Message)

#######################################
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("iin", "first_name", "last_name",)
    list_display_links = (
        "iin",
    )
    # list_editable = ("is_active",)
    list_filter = ("iin", "first_name", "last_name",)
    fieldsets = (
        (
            "Основная индексация",
            {"fields": ("iin",)},
        ),
        (
            "Техническое",
            {"fields": ("first_name", "last_name")},
        ),
    )
    search_fields = ["iin", "first_name", "last_name",]

admin.site.register(models.Worker, WorkerAdmin)
# admin.site.register(models.Worker)
admin.site.register(models.News)
admin.site.register(models.Rating)
admin.site.register(models.UserProfile)