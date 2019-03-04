from django.contrib import admin
from .models import Link

# Register your models here.
class AdminLink(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
             # Comprobara si dentro de el grupo personal existe el usuario
            return('name',)
        else:
            return ('created', 'updated')

    def get_exclude(self, request, obj=None):
         if request.user.groups.filter(name="Personal").exists():
             # Comprobara si dentro de el grupo personal existe el usuario
            return('key',)

admin.site.register(Link, AdminLink)
