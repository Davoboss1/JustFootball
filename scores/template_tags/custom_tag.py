from django import template
register = template.Library()
@register.filter
def filters(value,filter_items):
	return value.filter(leagues_table=filter_items)

register.filter("filters",filters)


@register.filter	
def cut(value,arg):
	return value.filter(leagues_table=arg)
    
    
