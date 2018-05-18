from django import template

from wagtail.core.models import Page

from ..models import FooterText


register = template.Library()


@register.inclusion_tag('phi/include/footer_text.html', takes_context=True)
def get_footer_text(context):
	footer_text = ''
	if FooterText.objects.first() is not None:
		footer_text = FooterText.objects.first().body

	return {
		'footer_text': footer_text,
	}