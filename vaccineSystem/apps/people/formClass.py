from .models import People


class PersonForm:
    def __init__(self, ci=None, name="", last_names="", sex="", age="", address="", consulting_room_id="", consulting_room_name="", positive_pcr=False, date_pcr=""):
        self.ci = ci
        self.name = name
        self.last_names = last_names
        self.sex = sex
        self.age = age
        self.address = address
        self.consulting_room_id = consulting_room_id
        self.consulting_room_name = consulting_room_name
        self.positive_pcr = positive_pcr
        self.date_pcr = date_pcr

    def updateValues(self, people: People):
        self.ci = people.ci
        self.name = people.name
        self.last_names = people.last_names
        self.sex = people.sex
        self.age = str(people.age)
        self.address = people.address
        self.consulting_room_id = people.consulting_room.pk
        self.consulting_room_name = people.consulting_room.name
        self.positive_pcr = people.positive_pcr
        self.date_pcr = str(people.date_pcr)
    
    def __str__(self):
        return str(self.__dict__)
