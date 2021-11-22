class ProvinceForm:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    

class MunicipalityForm:
    def __init__(self, id, name, provinceId):
        self.__id = id
        self.__name = name
        self.__provinceId = provinceId

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def provinceId(self):
        return self.__provinceId

    @provinceId.setter
    def provinceId(self, value):
        self.__provinceId = value