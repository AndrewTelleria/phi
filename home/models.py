from django import forms
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    class Meta:
    	verbose_name = "homepage"

    content_panels = Page.content_panels + [
    	FieldPanel('body', classname="full"),
    	InlinePanel('gallery_images', label="Gallery images"),
    ]


class HomePageImageGallery(Orderable):
	page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ForeignKey(
			'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
		)
	caption = models.CharField(blank=True, max_length=250)
	logo = models.BooleanField(default=False)

	panels = [
		ImageChooserPanel('image'),
		FieldPanel('caption'),
		FieldPanel('logo', widget=forms.RadioSelect),
	]
