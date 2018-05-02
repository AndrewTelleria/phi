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
	body = RichTextField()

	panels = [
		FieldPanel('body'),
	]

	def __str__(self):
		return "Footer text"

	class Meta:
		verbose_name_plural = "Footer Text"


