## tags.py
from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''

class NavSelectedNode(template.Node):
    def __init__(self, patterns):
        self.patterns = patterns
    def render(self, context):
        path = context['request'].path
        for p in self.patterns:
            pValue = template.Variable(p).resolve(context)
            if path == pValue:
                return "-active"
        return ""