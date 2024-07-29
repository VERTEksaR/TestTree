from django import template

from app.models import Menu

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(name_menu):
    """Функция по созданию меню"""
    alla = []
    item = Menu.objects.filter(url_name=name_menu).select_related('parent')[0]
    check_children(item, alla)
    return {"items": alla}


def check_children(aaa, alla):
    """Функция для добавления всех элементов меню в единый список"""
    alla.append(aaa)
    if aaa.children.exists():
        for gg in aaa.children.all():
            check_children(gg, alla)
