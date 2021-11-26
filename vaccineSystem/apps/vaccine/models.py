from django.db import models
from ..people.models import People
from ..locality.models import ConsultingRoom, School


class Vaccine(models.Model):
    name = models.CharField(max_length=255, unique=True)
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

    def save(self, *args, **kwargs):
        self.validate_unique()
        super(Vaccine, self).save(*args, **kwargs)


""" Vaccination """


class Vaccination(models.Model):
    people = models.ForeignKey(People, on_delete=models.PROTECT, related_name='vaccinations')
    vaccine = models.ForeignKey(Vaccine, on_delete=models.PROTECT, related_name='vac_vaccinations')
    adverse_reactions = models.TextField()
    

class PersonalHealth_Vaccination(Vaccination):
    health_category = models.CharField(max_length=255)

class ConsultingRoom_Vaccination(Vaccination):
    consulting_rooms = models.ForeignKey(ConsultingRoom, on_delete=models.PROTECT, related_name='con_vaccinations')

class School_Vaccination(Vaccination):
    school = models.ForeignKey(School, on_delete=models.PROTECT, related_name='school_vaccinations')

class Doce(models.Model):
    lot = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    vaccination = models.ForeignKey(Vaccination, on_delete=models.PROTECT, related_name='doses')