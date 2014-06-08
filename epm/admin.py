from django.contrib import admin
from epm.models import *
from import_export.admin import ImportExportMixin
from epm.resource import *

# Register your models here.
class PartyAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = PartyResource

admin.site.register(enterprise)
admin.site.register(party,PartyAdmin)
