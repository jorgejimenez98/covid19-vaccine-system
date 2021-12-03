from datetime import date


def getNotExistUserError(user: str) -> str:
    return f'No existe una cuenta con el nombre de usuario ({user})'


def getNoAdminDeleteMessage(username) -> str:
    message = f'Lo sentimos. El usuario {username} es el único administrador, no puede dejar el sistema sin ' \
              f'administradores'
    return message


def deleteSuccessMessage(username) -> str:
    message = f'El usuario {username} ha sido eliminado satisfactoriamente'
    return message


def getUniqueUserError(user: str) -> str:
    return f'Ya existe una cuenta con el nombre de usuario ({user})'


def getSuccessCreatedMessage(type: str) -> str:
    return f'{type} creado satisfactoriamente'


def getSuccessEditMessage(type: str) -> str:
    return f'{type} editado satisfactoriamente'


def getUniqueTypeError(type: str, name: str) -> str:
    return f'Ya existe una {type} con el nombre ({name})'


def getDelSuccessText(type: str, name: str) -> str:
    return f'{type} ({name}) eliminada satisfactoriamente'


def getDeleSuccessText(type: str) -> str:
    return f'{type} eliminada satisfactoriamente'


def getDelProtectText(type: str, name: str) -> str:
    return f'No se puede eliminar la {type} ({name}) porque otras entidades dependen de él'


def getUniqueModelError(type: str, name: str) -> str:
    return f'Ya existe una {type} con el nombre ({name})'


def getUniqueCIError(type: str, name: str) -> str:
    return f'Ya existe una {type} con el CI ({name})'


def getOnlyOneBoolError() -> str:
    return "Debes seleccionar solo un tipo de disponibilidad"


def getNoDatePcr() -> str:
    return "Si la persona tiene un pcr positivo debe insertar la fecha del mismo"


def getNoPcrSelect() -> str:
    return "Debes checkear el pcr positivo ya que has insertado una fecha"


""" Date Funcitons """


def getDateFromString(value: str) -> date:
    auxArray = value.split('-')
    return date(int(auxArray[0]), int(auxArray[1]), int(auxArray[2]))


""" Validate CI """


def validateCI(ci: str):
    year, month, day = int(ci[0:2]), int(ci[2:4]), int(ci[4:6])
    if year not in range(0, 100):
        raise Exception("El año del CI debe estar entre 00 y 99")
    if month not in range(1, 13):
        raise Exception("El mes del CI debe estar entre 1 y 12")
    if day not in range(1, 32):
        raise Exception("El dia del CI debe estar entre 1 y 31")