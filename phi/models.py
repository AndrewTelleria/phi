from django import forms
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class FooterText(models.Model):
	"""
	This provides editable text for the site footer. Again it uses the decorator
	'register_snippet' to allow it to be accessible via the admin. It is made
	accessible on the template via a template tag defined in templates/phi/templatetags/
	navigation_tags.py
	"""
	body = RichTextField()

	pangels = [
		FieldPanel('body'),
	]

	def __str__(self):
		return "Footer text"

	class Meta:
		verbose_name_plural = "Footer Text"