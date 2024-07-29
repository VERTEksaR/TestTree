from django.shortcuts import render


def draw_menu(request, name_menu):
    context = {"name": name_menu}
    return render(request=request, template_name='base.html', context=context)
