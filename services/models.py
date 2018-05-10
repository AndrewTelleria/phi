from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index

from home.blocks import BaseStreamBlock


class ServiceIndexPage(Page):
	body = StreamField(
		BaseStreamBlock(), verbose_name="Page body", blank=True
	)

	content_panels =  Page.content_panels + [
		StreamFieldPanel('body'),
	]


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
	service = models.CharField(max_length=255)
	price = models.FloatField(default=True)
	body = StreamField(
		BaseStreamBlock(), verbose_name="Page body", blank=True
	)

	def feature_order(self, request):
		sp_list = [1, 2, 3, 4]
		objs = self.objects.all()
		for sp in objs:
			for value in sp_list:
				if value == sp.feature and sp not in sp_list:
					sp_list.insert(value-1, sp)
					sp_list.remove(value)
		context = {
			'features_list': sp_list,
		}
		return render(request, 'home/home_page.html', context)


	def animal_type(self):
		return self.animal

	search_fields = Page.search_fields + [
        index.SearchField('service'),
        index.SearchField('price'),
    ]

	content_panels = Page.content_panels + [
		FieldPanel('animal'),
		FieldPanel('feature'),
		FieldPanel('service'),
		FieldPanel('price'),
		StreamFieldPanel('body'),
    ]



