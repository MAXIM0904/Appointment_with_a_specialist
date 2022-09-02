from django.contrib import admin
from .models import DataRecord, Client


class DataRecordAdmin(admin.ModelAdmin):
    pass

class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(DataRecord, DataRecordAdmin)
admin.site.register(Client, ClientAdmin)
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
