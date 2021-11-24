from django.db import models
from ..locality.models import ConsultingRoom

class People(models.Model):
    ci = models.CharField(max_length=11, primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    last_names = models.CharField(max_length=255)
    sex = models.CharField(max_length=1)
    age = models.PositiveIntegerField()
    address = models.TextField()
    consulting_room = models.ForeignKey(ConsultingRoom, on_delete=models.PROTECT, related_name='persons')
    positive_pcr = models.BooleanField(default=False, null=True, blank=True)
    date_pcr = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.last_names} - {self.ci}'

