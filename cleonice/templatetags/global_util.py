# -*- coding: utf-8 -*-
from django import template
import datetime

register = template.Library()


"""""""""
 Math Operations
"""""""""
@register.filter(name='mod')
def mod(value, arg):
	if value % arg == 0:
		return True
	else:
		return False


"""""""""
 Outhers
"""""""""

@register.tag(name='current_time')
def do_current_time(parser, token):
	try:
		# split_contents() do not konw how to divide the string
		tag_name, format_string = token.split_contents()
	except ValueError:
		msg = '%r tag requer um argumento simples' % token.split_contents()[0]
		raise template.TemplateSyntaxError(msg)
	return CurrentTimeNode(format_string[1:-1])


class CurrentTimeNode(template.Node):
	def __init__(self, format_string):
		self.format_string = str(format_string)

	def render(self, context):
		now = datetime.datetime.now()
		return now.strftime(self.format_string)