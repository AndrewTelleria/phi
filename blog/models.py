from django.db import models

from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import (
    FieldPanel, 
    InlinePanel, 
    MultiFieldPanel, 
    StreamFieldPanel,
)

from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    class Meta:
    	verbose_name = "blog indexpage"
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    subpage_types = ['Blogpage']


    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        # Get the full unpaginated listing of resource pages as a queryset
        all_resources = BlogPage.objects.descendant_of(
            self).live().order_by(
            '-first_published_at')
        paginator = Paginator(all_resources, 5)
        page = request.GET.get('page')
        try:            
            resources = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            resources = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            resources = paginator.page(paginator.num_pages)
        context['resources'] = resources
        return context


class BlogPageTag(TaggedItemBase):

    class Meta:
        verbose_name = "blogpage tag"

    content_object = ParentalKey(
            'BlogPage',
            related_name='tagged_items',
            on_delete=models.CASCADE
        )


class BlogPage(Page):
    author = models.ForeignKey(
        'home.People',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
        ])
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    class Meta:
        verbose_name = "blogpage"

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('author'),
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        SnippetChooserPanel('author'),
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
            'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
        )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class BlogTagIndexPage(Page):

	class Meta:
		verbose_name = "blogtag indexpage"

	def get_context(self, request):

		# Filter by tag
		tag = request.GET.get('tag')
		blogpages = BlogPage.objects.filter(tags__name=tag)

		# Update template context
		context = super().get_context(request)
		context['blogpages'] = blogpages
		return context



@register_snippet
class BlogCategory(models.Model):
	name = models.CharField(max_length=255)
	icon = models.ForeignKey(
			'wagtailimages.Image', null=True, blank=True,
			on_delete=models.SET_NULL, related_name='+'
		)

	panels = [
		FieldPanel('name'),
		ImageChooserPanel('icon'),
	]

	def __str__(self):
		return self.name









