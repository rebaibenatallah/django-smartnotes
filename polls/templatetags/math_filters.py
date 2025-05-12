from django import template

register = template.Library()

@register.filter
def percentage(value ,arg):
    try:
        return int( int(value) / int(arg) *100 )
    except(ValueError, TypeError):
        return ''