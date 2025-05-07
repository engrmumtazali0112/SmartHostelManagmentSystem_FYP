from django import template
from itertools import groupby
from operator import itemgetter
from django.db.models import Sum

register = template.Library()

# Filter to access dictionary items by key
@register.filter(name='get_item')
def get_item(dictionary, key):
    """
    Filter to access dictionary items by key in Django templates.
    Usage: {{ my_dict|get_item:my_key }}
    """
    if dictionary is None:
        return None
    return dictionary.get(key)


# Filter to multiply value by a multiplier
@register.filter
def multiply(value, multiplier):
    try:
        return float(value) * float(multiplier)
    except (ValueError, TypeError):
        return 0  # Return 0 if the value or multiplier is invalid

# Custom filter to multiply two values
@register.filter
def mul(value, arg):
    try:
        return value * arg
    except (TypeError, ValueError):
        return value

# Filter to calculate the total amount of all bills in a queryset
@register.filter
def bill_total_amount(bills):
    """Calculate the total amount of all bills in a queryset"""
    return bills.aggregate(Sum('total_amount'))['total_amount__sum'] or 0


# Filter to calculate the total price of all meals
@register.filter
def meal_price_total(meal_details):
    """Calculate the total price of all meals"""
    return sum(meal['price'] for meal in meal_details)


# Filter to subtract the arg from the value
@register.filter
def sub(value, arg):
    """Subtract the arg from the value"""
    return value - arg


# Filter to group a list of dictionaries by a given key
@register.filter
def regroup_by(value, arg):
    """
    Group a list of dictionaries by a given key.
    Usage: {{ my_list|get_item:'key'|regroup_by:'key' }}
    """
    grouped = groupby(sorted(value, key=itemgetter(arg)), key=itemgetter(arg))
    return {key: list(group) for key, group in grouped}
