from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
	CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
)


class ImageBlock(StructBlock):
	"""
	Customer 'StructBlock' for utilizing images with associated caption and attribution data
	"""
	image = ImageChooserBlock(required=True)
	caption = CharBlock(required=False)
	attribution = CharBlock(required=False)

	class Meta:
		icon = 'image'
		template = 'home/blocks/image_block.html'


class HeadingBlock(StructBlock):
	"""
	Custom 'StructBlock' that allows user to select h2 - h4 sizes for headers
	"""
	heading_text = CharBlock(classname="title", required=True)
	size = ChoiceBlock(choices=[
		('', 'Select a header size'),
		('h2', 'H2'),
		('h3', 'H3'),
		('h4', 'H4'),
	], blank=True, required=False)

	class Meta:
		icon = "title"
		template = "home/blocks/heading_block.html"


class BlockQuote(StructBlock):
	"""
	Custom 'StructBlock' that allows the user to attribute a quote to the author
	"""
	text = TextBlock()
	attribute_name = CharBlock(
		blank=True, required=False, label='e.g. Mary Berry')

	class Meta:
		icon = 'fa-quote-left'
		template = 'home/blocks/blockquote.html'

# StreamBlocks
class BaseStreamBlock(StreamBlock):
	"""
	Define the custom blocks that 'StreamField' will utilize
	"""
	heading_block = HeadingBlock()
	paragraph_block = RichTextBlock(
		icon="fa-paragraph",
		template = "home/blocks/paragraph_block.html"
	)
	image_block = ImageBlock()
	block_quote = BlockQuote()
	embed_block = EmbedBlock(
		help_text='Insert an embed URL e.g. https://www.youtube.com/embed/SGJFWirQ3ks',
		icon="fa-s15",
		template="home/blocks/embed_block.html"
	)


