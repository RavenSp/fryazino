from django import template
from simplepage.models import TextBlock

register = template.Library()

@register.inclusion_tag('tags/text_block.html')
def textblock(key):

    textblock = TextBlock.objects.get(key=key)

    return {'textblock':textblock}