class VaccineForm:
    def __init__(self, id=None, name="", healthPersonnel=False, canConsultingRoom=False, canSchool=False):
        self.id = id
        self.name = name
        self.healthPersonnel = healthPersonnel
        self.canConsultingRoom = canConsultingRoom
        self.canSchool = canSchool

    def updateValues(self, vaccine):
        self.id = vaccine.id
        self.name = vaccine.name
        self.healthPersonnel = vaccine.healthPersonnel
        self.canConsultingRoom = vaccine.canConsultingRoom
        self.canSchool = vaccine.canSchool


class SchoolVaccineForm:
    def __init__(self, id=None, vaccineId='', badReaction=False, schoolId=""):
        self.id = id
        self.vaccineId = vaccineId
        self.badReaction = badReaction
        self.schoolId = schoolId

    def updateValues(self, vaccination):
        self.id = vaccination.pk
        self.vaccineId = vaccination.vaccine.id
        self.badReaction = vaccination.has_adverse_reactions
        self.schoolId = vaccination.school.id

class ConsultginVaccineForm:
    def __init__(self, id=None, vaccineId='', badReaction=False, consultingId=""):
        self.id = id
        self.vaccineId = vaccineId
        self.badReaction = badReaction
        self.consultingId = consultingId

    def updateValues(self, vaccination):
        self.id = vaccination.pk
        self.vaccineId = vaccination.vaccine.id
        self.badReaction = vaccination.has_adverse_reactions
        self.consultingId = vaccination.consulting_rooms.id

class HealthVaccineForm:
    def __init__(self, id=None, vaccineId='', badReaction=False, haelthCategory=""):
        self.id = id
        self.vaccineId = vaccineId
        self.badReaction = badReaction
        self.haelthCategory = haelthCategory

    def updateValues(self, vaccination):
        self.id = vaccination.pk
        self.vaccineId = vaccination.vaccine.id
        self.badReaction = vaccination.has_adverse_reactions
        self.haelthCategory = vaccination.health_category
