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
