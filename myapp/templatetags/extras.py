from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def set_page(context, page):
    query = context['request'].GET.copy()
    query['page'] = page
    return query.urlencode()
