from django import template

register = template.Library()


@register.filter(name='isRol')
def isRol(user, rol):
    return user.rol == rol
