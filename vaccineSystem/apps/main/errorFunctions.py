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
    print(value)
    auxArray = value.split('-')
    return date(int(auxArray[0]), int(auxArray[1]), int(auxArray[2]))