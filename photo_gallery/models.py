from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class PhotoGalleryIndexPage(Page):
	intro = RichTextField(blank=True)

	class Meta:
		verbose_name = "photo gallery indexpage"

	def get_context(self, request):
		# Update context to include only published posts, ordered by reverse-chron
		context = super().get_context(request)
		photo_gallery_pages = self.get_children().live().order_by('-first_published_at')
		context['photo_gallery_pages'] = photo_gallery_pages
		return context

	content_panels = Page.content_panels + [
		FieldPanel('intro', classname="photo-gallery")
	]


class PhotoGalleryPage(Page):
	date = models.DateField("Post date")
	description = models.CharField(max_length=1000)

	def main_image(self):
		gallery_item = self.gallery_images.first()
		if gallery_item:
			return gallery_item.image
		else:
			return None


	search_fields = Page.search_fields + [
		index.SearchField('date'),
		index.SearchField('description'),
	]

	content_panels = Page.content_panels + [
		FieldPanel('date'),
		FieldPanel('description'),
		InlinePanel('gallery_images', label="Gallery images"),
	]


class PhotoGalleryImage(Orderable):
	page = ParentalKey(PhotoGalleryPage, on_delete=models.CASCADE, related_name="gallery_images")
	image = models.ForeignKey(
			'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
		)
	caption = models.CharField(blank=True, max_length=250)

	panels = [
		ImageChooserPanel('image'),
		FieldPanel('caption'),
	]



