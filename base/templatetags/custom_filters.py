from django import template

register = template.Library()

@register.filter
def split(value, delimiter):
    """Splits a string by the given delimiter."""
    if isinstance(value, str):  # Ensure that the value is a string
        return value.split(delimiter)
    return value