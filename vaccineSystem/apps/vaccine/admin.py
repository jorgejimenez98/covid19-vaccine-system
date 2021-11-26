from django.contrib import admin
from .models import Vaccine, ConsultingRoom_Vaccination, School_Vaccination, PersonalHealth_Vaccination, Doce

admin.site.register(Vaccine)
admin.site.register(PersonalHealth_Vaccination)
admin.site.register(School_Vaccination)
admin.site.register(ConsultingRoom_Vaccination)
admin.site.register(Doce)
