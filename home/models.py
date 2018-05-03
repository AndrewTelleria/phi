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


class StandardPage(Page):
	"""
	A generic content page. On this demo site we use it for an about page but
	it could be used for any page content that only needs a title,
	image, introduction, and body field
	"""

	introduction = models.TextField(
			help_text='Text to describe the page',
			blank=True,
		)
	image = models.ForeignKey(
			'wagtailimages.Image',
			null=True,
			blank=True,
			on_delete=models.SET_NULL,
			related_name='+',
			help_text='Landscape mode only; horizontal width between 1000px and 3000px'
		)
	# body = StreamField(
	# 		BaseStreamBlock(), verbose_name="Page body", blank=True
	# 	)
	content_panels = Page.content_panels + [
		FieldPanel('introduction', classname="full"),
		# StreamFieldPanel('body'),
		ImageChooserPanel('image'),
	]



class HomePage(Page):
    """
	The Home Page. This looks slightly more complicated then it is. You can see
	if you visit your site and edit the homepage that it is split between a:
		- Hero area
		- Body area
		- A promotional area
		- Moveable feature site sections
    """

    # Hero section of HomePage
    image = models.ForeignKey(
    		'wagtailimages.Image',
    		null=True,
    		blank=True,
    		on_delete=models.SET_NULL,
    		related_name='+',
    		help_text='Homepage image',
    	)
    hero_text = models.CharField(
    		max_length=255,
    		help_text='Write an introduction for the bakery',
    	)
    hero_cta = models.CharField(
    		verbose_name='Hero CTA',
    		max_length=255,
    		help_text='Text to display on Call to Action',
    	)
    hero_cta_link = models.ForeignKey(
    		'wagtailcore.Page',
    		null=True,
    		blank=True,
    		on_delete=models.SET_NULL,
    		related_name='+',
    		verbose_name='Hero CTA link',
    		help_text='Choose a page to link to for the Call to Action',
    	)

    # Body section of the HomePage
    # body = StreamField(
    # 		BaseStreamBlock(), verbose_name="Home content block", blank=True
    # 	)

    # Promo section of the HomePage
    promo_image = models.ForeignKey(
    		'wagtailimages.Image',
    		null=True,
    		blank=True,
    		on_delete=models.SET_NULL,
    		related_name='+',
    		help_text='Promo image',
    	)
    promo_title = models.CharField(
    		null=True,
    		blank=True,
    		max_length=255,
    		help_text='Title to display above the promo copy',
    	)
    promo_text = RichTextField(
    		null=True,
    		blank=True,
    		help_text='Write some promotional copy',
    	)

    # Featured sections on the HomePage
    # You will see on templates/home/home_page.html that these are treated
    # in different ways, and displayed in different areas of the page.
    # Each list their children items that we access via the children function
    # that we define on the individual Page models e.g. BlogIndexPage
    featured_section_1_title = models.CharField(
    		null=True,
    		blank=True,
    		max_length=255,
    		help_text='Title to display above the promo copy',
    	)
    featured_section_1 = models.ForeignKey(
    		'wagtailcore.Page',
    		null=True,
    		blank=True,
    		on_delete=models.SET_NULL,
    		related_name='+',
    		help_text='First featured section for the homepage. Will display up to '
    		'three child names.',
    		verbose_name='Featured section 1',
    	)

    content_panels = Page.content_panels + [
    	MultiFieldPanel([
    		ImageChooserPanel('image'),
    		FieldPanel('hero_text', classname="full"),
    		MultiFieldPanel([
    			FieldPanel('hero_cta'),
    			PageChooserPanel('hero_cta_link'),
    			]),
    		], heading="Hero section"),
    	MultiFieldPanel([
    		ImageChooserPanel('promo_image'),
    		FieldPanel('promo_title'),
    		FieldPanel('promo_text'),
    		], heading="Promo section"),
    	# StreamFieldPanel('body'),
		MultiFieldPanel([
			FieldPanel('featured_section_1_title'),
			PageChooserPanel('featured_section_1'),
			], heading="Featured homepage section", classname="collapsible")
    ]

    def __str__(self):
    	return self.title



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
