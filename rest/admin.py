from django.contrib import admin

# Register your models here.
from rest.models import *

admin.site.register(Album)
admin.site.register(Track)
