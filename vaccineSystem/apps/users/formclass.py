class UserForm:
    def __init__(self, name, username, rol, password, confirmPassword):
        self.__name = name
        self.__username = username
        self.__rol = rol
        self.__password = password
        self.__confirmPassword = confirmPassword

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def rol(self):
        return self.__rol

    @rol.setter
    def rol(self, value):
        self.__rol = value

    @property
    def password(self):
        return self.__password

    @rol.setter
    def password(self, value):
        self.__password = value

    @property
    def confirmPassword(self):
        return self.__confirmPassword

    @rol.setter
    def confirmPassword(self, value):
        self.__confirmPassword = value
