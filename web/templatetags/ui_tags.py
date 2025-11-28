from django import template

register = template.Library()

@register.inclusion_tag('ui/button.html')
def ui_button(text="", variant="default", size="default", type="button", css_class="", href=None, disabled=False):
    return {
        'text': text,
        'variant': variant,
        'size': size,
        'type': type,
        'class': css_class,
        'href': href,
        'disabled': disabled,
    }

@register.inclusion_tag('ui/card.html')
def ui_card(css_class=""):
    return {'class': css_class}

@register.inclusion_tag('ui/input.html')
def ui_input(name, type="text", placeholder="", value="", id=None, css_class="", required=False, disabled=False):
    return {
        'name': name,
        'type': type,
        'placeholder': placeholder,
        'value': value,
        'id': id or name,
        'class': css_class,
        'required': required,
        'disabled': disabled,
    }

@register.inclusion_tag('ui/label.html')
def ui_label(text, for_id, css_class=""):
    return {
        'text': text,
        'for_id': for_id,
        'class': css_class,
    }

@register.inclusion_tag('ui/select.html')
def ui_select(name, options, placeholder="Select an option", id=None, css_class="", required=False, size="default"):
    return {
        'name': name,
        'options': options,
        'placeholder': placeholder,
        'id': id or name,
        'class': css_class,
        'required': required,
        'size': size,
    }

@register.inclusion_tag('ui/image_fallback.html')
def ui_image_fallback(src, alt, css_class="", fallback_src="/static/images/placeholder.jpg"):
    return {
        'src': src,
        'alt': alt,
        'class': css_class,
        'fallback_src': fallback_src,
    }
