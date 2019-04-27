from django import template
register = template.Library()

@register.filter
def filters(value,filter_items):
	return value.filter(leagues_table=filter_items)

