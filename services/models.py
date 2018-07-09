from django.db import models
from django.core.validators import RegexValidator

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from home.blocks import BaseStreamBlock

# from home.models import HomePage


class ServiceIndexPage(Page):
	body = StreamField(
		BaseStreamBlock(), verbose_name="Page body", blank=True
	)

	content_panels =  Page.content_panels + [
		StreamFieldPanel('body'),
	]

	# def get_context(self, request):
	# 	context = super(ServiceIndexPage, self).get_context(request)
	# 	home_page = Page.objects.parent_of(self).live()



class ServicePage(Page):
	CAT = 'cat'
	DOG = 'dog'
	ANIMAL_CHOICES = (
		(CAT, 'Cat'),
		(DOG, 'Dog'),
	)
	animal = models.CharField(
		max_length=15,
		choices=ANIMAL_CHOICES,
		default=DOG,
	)
	FEATURE_1 = 1
	FEATURE_2 = 2
	FEATURE_3 = 3
	FEATURE_4 = 4
	NO_FEATURE = 0
	FEATURE_CHOICES = (
		(FEATURE_1, 'Feature 1'),
		(FEATURE_2, 'Feature 2'),
		(FEATURE_3, 'Feature 3'),
		(FEATURE_4, 'Feature 4'),
		(NO_FEATURE, 'No feature')
	)
	feature = models.IntegerField(
		choices=FEATURE_CHOICES,
		default=0,
	)
	image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+',
		help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
	)
	service = models.CharField(max_length=255)
	display_price = models.CharField(max_length=255, help_text='Ex. $50/day', default='$0.00')
	price = models.DecimalField(max_digits=6, decimal_places=2, help_text='50.00', default=0.00)
	body = StreamField(
		BaseStreamBlock(), verbose_name="Page body", blank=True
	)

	def animal_type(self):
		return self.animal

	def main_image(self):
		return self.image

	search_fields = Page.search_fields + [
        index.SearchField('service'),
        index.SearchField('price'),
    ]

	content_panels = Page.content_panels + [
		FieldPanel('animal'),
		FieldPanel('feature'),
		FieldPanel('service'),
		FieldPanel('price'),
		FieldPanel('display_price'),		
		ImageChooserPanel('image'),
		StreamFieldPanel('body'),
    ]



