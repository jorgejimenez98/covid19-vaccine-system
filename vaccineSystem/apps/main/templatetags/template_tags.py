from django import template

register = template.Library()


@register.filter(name='isRol')
def isRol(user, rol):
    return user.rol == rol


@register.filter(name='isProvinceId')
def isProvinceId(province, provinceId):
    return province.pk == provinceId


@register.filter(name='isSex')
def isSex(person, sex):
    return person.sex == sex
