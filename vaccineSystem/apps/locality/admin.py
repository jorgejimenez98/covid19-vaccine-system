from django.contrib import admin
from .models import Province, Municipality, School, Polyclinic

admin.site.register(Province)
admin.site.register(Municipality)
admin.site.register(School)
admin.site.register(Polyclinic)
