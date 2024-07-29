from django import template

from app.models import Menu

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(name_menu):
    """Функция по созданию меню"""
    list_of_units = []
    item = Menu.objects.filter(url_name=name_menu).select_related('parent')[0]
    check_children(item, list_of_units)
    return {"items": list_of_units}


def check_children(unit, list_of_units):
    """Функция для добавления всех элементов меню в единый список"""
    list_of_units.append(unit)
    if unit.children.exists():
        for item in unit.children.all():
            check_children(item, list_of_units)
