from django import template 

register = template.Library()


# Here dict, key are the arguments replyDict|get_val:comment.sno and get_val is the function.
@register.filter(name='get_val')
def get_val(dict, key):
    return dict.get(key)