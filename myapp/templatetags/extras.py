from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def page_link(context, page):
    query = context['request'].GET.copy()
    query['page'] = page
    return query.urlencode()