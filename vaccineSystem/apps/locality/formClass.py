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
    def __init__(self, id, name, provinceId, provinceName):
        self.__id = id
        self.__name = name
        self.__provinceId = provinceId
        self.__provinceName = provinceName

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

    @property
    def provinceName(self):
        return self.__provinceName

    @provinceName.setter
    def provinceName(self, value):
        self.__provinceName = value