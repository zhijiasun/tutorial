from epm.models import *
from import_export import resources

class PartyResource(resources.ModelResource):
    class Meta:
        model = party
        exclude = ('party_id',)
