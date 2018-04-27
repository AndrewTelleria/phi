from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class AboutPage(Page):
	body = RichTextField(blank=True)

	class Meta:
		verbose_name = "aboutpage"

	content_panels = Page.content_panels + [
		FieldPanel('body', classname="full")
	]


class ContactPage(Page):
	body = RichTextField(blank=True)

	class Meta:
		verbose_name = "contactpage"

	content_panels = Page.content_panels + [
		FieldPanel('body', classname="full")
	]


class DogServicePage(Page):
	body = RichTextField(blank=True)

	class Meta:
		verbose_name = "dog servicepage"

	content_panels = Page.content_panels + [
		FieldPanel('body', classname="full")
	]

class CatServicePage(Page):
	body = RichTextField(blank=True)

	class Meta:
		verbose_name = "cat servicepage"

	content_panels = Page.content_panels + [
		FieldPanel('body', classname="full")
	]







