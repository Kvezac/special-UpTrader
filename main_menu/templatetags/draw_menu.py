from django import template

from main_menu.models import Menu

register = template.Library()


@register.inclusion_tag('tags/menu_tag.html', takes_context=True)
def draw_menu(context, name):
    main_menu = Menu.objects.filter(parent__isnull=True, name=name).prefetch_related('children')
    result = {'main_menu': main_menu}
    return result
