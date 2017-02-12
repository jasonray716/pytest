import datetime
from django import template

register = template.Library()

@register.filter
def eligible(birthday):
   birthday = datetime.datetime.combine(birthday, datetime.time(0, 0))
   base_date = datetime.datetime.now() - datetime.timedelta(days=365*13)
   if birthday < base_date:
       return 'allowed'
   else:
       return 'blocked'


