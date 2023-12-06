from django.contrib import admin
from storage.models import *


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    fields = ['name',
              'qty']