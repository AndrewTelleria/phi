from django import forms
from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
		FieldPanel,
		FieldRowPanel,
		InlinePanel,
		MultiFieldPanel,
		PageChooserPanel,
		StreamFieldPanel,
	)

from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Collection, Page, Orderable
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

# from .blocks import BaseStreamBlock


@register_snippet
class People(ClusterableModel):
	"""
	A Django model to store people objects. It uses the '@register_snippet'
	decorator to allow it to be accesible via the Snippets UI

	'People' uses the 'ClusterableModel', which allows the relationship with
	another model to be stored locally to the 'parent' model (e.g. a PageModel)
	until the parent is explicitly saved. This allows the editor to use the
	'Preview' button, to preview the content, without saving the relationships
	to the database.
	https://github.com/wagtail/django-modelcluster
	"""
	first_name = models.CharField("First name", max_length=254)
	last_name = models.CharField("First name", max_length=254)
	job_title = models.CharField("First name", max_length=254)

	image = models.ForeignKey(
			'wagtailimages.Image',
			null=True,
			blank=True,
			on_delete=models.SET_NULL,
			related_name='+',
		)

	panels = [
		FieldPanel('first_name', classname="first-name"),
		FieldPanel('last_name', classname="last-name"),
		FieldPanel('job_title'),
		ImageChooserPanel('image'),
	]

	search_fields = Page.search_fields + [
		index.SearchField('first_name'),
		index.SearchField('last_name'),
	]

	@property
	def thumb_image(self):
		# Returns an empty string if there is no profile pic or the rendition
		# file can't be found.
		try:
			return self.image.get_rendition('fill-50x50').img_tag()
		except:
			return ''

	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)

	class Meta:
		verbose_name = 'Person'
		verbose_name_plural = 'People'

@register_snippet
class FooterText(models.Model):
	"""
	This provides editable text for the site footer. Again it uses the decorator
	'register_snippet' to allow it to be accessible via the admin. It is made
	accessible on the template via a template tag defined in templates/home/templatetags/
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
