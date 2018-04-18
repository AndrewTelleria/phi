from django import forms
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

class PhiPage(Page):


	content_panels = Page.content_panels + [
    	InlinePanel('logo', label="Logo image"),
    ]

class PhiPageLogo(Orderable):
	page = ParentalKey(PhiPage, on_delete=models.CASCADE, related_name='logo')
	image = models.ForeignKey(
			'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
		)
	caption = models.CharField(blank=True, max_length=250)

	panels = [
		ImageChooserPanel('image'),
		FieldPanel('caption'),
	]