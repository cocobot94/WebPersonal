from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from Core.models import Link, Acerca, Yo, Info


# Register your models here.
class linkAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

    def get_readonly_fields(self, request, obj: None):
        if not request.user.is_staff:
            return ("key", "created", "updated")
        return ("created", "updated")

    list_display = ("title",)


class acercaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

    list_display = ("title", "created", "updated")


class yoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

    list_display = ("name", "created", "updated")


class infoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

    list_display = ("telephone", "email", "created", "updated")


admin.site.register(Link, linkAdmin)
admin.site.register(Acerca, acercaAdmin)
admin.site.register(Yo, yoAdmin)
admin.site.register(Info, infoAdmin)
