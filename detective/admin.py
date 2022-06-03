from django.contrib import admin

from .models import Place, Suspect, Weapon

admin.site.register(Suspect)
admin.site.register(Weapon)
admin.site.register(Place)
