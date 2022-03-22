from django.contrib import admin

from .models import Rain, Ground



class RainInline(admin.TabularInline):
    model = Rain
    extra = 1


class GroundAdmin(admin.ModelAdmin):
    inlines = (RainInline,)


# Register your models here.
admin.site.register(Rain)
admin.site.register(Ground, GroundAdmin)
