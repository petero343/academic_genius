from django import template

register = template.Library()

@register.filter
def dict_key(dictionary, key):
    """Returns the value from a dictionary for the given key."""
    try:
        return dictionary.get(key, None)
    except AttributeError:
        return None
