from django import template

register = template.Library()

@register.filter
def filt(queryset, filter_item):
    return queryset.filter(date=filter_item)
    
@register.filter
def filter_league(queryset, filter_item):
    return queryset.filter(league=filter_item)