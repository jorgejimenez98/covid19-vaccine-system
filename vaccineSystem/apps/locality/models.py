from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'Provincia {self.name}'


class Municipality(models.Model):
    name = models.CharField(max_length=255, unique=True)
    province = models.ForeignKey(
        Province, on_delete=models.PROTECT, related_name='municipalities')

    def __str__(self):
        return f'Municipio {self.name} - {self.province.name}'


class School(models.Model):
    name = models.CharField(max_length=255, unique=True)
    municipality = models.ForeignKey(
        Municipality, on_delete=models.PROTECT, related_name='schools')

    def __str__(self):
        return f'Escuela {self.name}'


class Polyclinic(models.Model):
    name = models.CharField(max_length=255, unique=True)
    municipality = models.ForeignKey(
        Municipality, on_delete=models.PROTECT, related_name='polyclinics')

    def __str__(self):
        return f'Escuela {self.name}'
