from django import template

register = template.Library()

@register.simple_tag
def translate(string):
    from googletrans import Translator
    translator = Translator()
    if string is None:
        data = ""
    
    else:
        d = translator.translate( string, dest="hi", src="auto")
        data = d.text
    return data