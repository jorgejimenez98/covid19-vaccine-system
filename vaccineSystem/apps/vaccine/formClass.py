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
