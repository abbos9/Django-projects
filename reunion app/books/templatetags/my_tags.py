from django import template
from translate import Translator

register = template.Library()

@register.filter(name="translete")
def translete(value, target_language='uz'):
    translator = Translator(to_lang=target_language)
    translated_text = translator.translate(value)
    return translated_text

@register.filter(name="to_upper")
def to_upper(value, arg):
    return value.upper()

@register.filter(name="to_lower")
def to_lower(value, range):
    return value[:range]