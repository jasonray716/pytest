from django import template

register = template.Library()

@register.filter
def bizzfuzz(num):
   if num % 15 == 0:
   	return 'BizzFuzz'
   elif num % 3 == 0:
   	return 'Bizz'
   elif num % 5 == 0:
   	return 'Fuzz'
   else:
   	return num


