from django.db import models


class Vaccine(models.Model):
    name = models.CharField(max_length=255)
    healthPersonnel = models.BooleanField(default=False)
    canConsultingRoom = models.BooleanField(default=False)
    canSchool = models.BooleanField(default=False)

    def __str__(self):
        return f'Vacuna {self.name}'

    def getPlace(self):
        if self.healthPersonnel:
            return 'Personal de Salud'
        elif self.canConsultingRoom:
            return 'Es por consultorio'
        else:
            return 'Es por escuela'
