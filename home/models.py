from django.db import models

from wagtail.models import Page
from wagtail.core.fields import RichTextField,StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel,StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class HomePage(Page):
    templates = "home/home_page.html"
    # max_count = 2
    text_banner= models.CharField(max_length=100, blank=True, null=True)
    sub_banner=RichTextField(features=["bold", "italic"], blank=True)
    image_banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,  #Home page is already exist
        blank=True, # it can not be blank
        on_delete=models.SET_NULL,
        related_name="+"
    )
    content_panels = Page.content_panels + [
        FieldPanel("text_banner"),
        FieldPanel("sub_banner"),
        ImageChooserPanel("image_banner"),
    ]

#The profile Page
class UserProfilePage(Page):
    templates = "home/user_profil_page.html"
    avatar = models.ForeignKey(
        "wagtailimages.Image",
        null=True,  #Home page is already exist
        blank=True, # it can not be blank
        on_delete=models.SET_NULL,
        related_name="+"
    )
    bio= models.CharField(
        max_length=100, 
        blank=True,
        null=True,
        default='I am a Software developer'
    )

    body = StreamField([
        ('photo', ImageChooserBlock(required=False)),
    ], verbose_name='Contenu')

    content_panels = Page.content_panels + [
        ImageChooserPanel("avatar"),
        FieldPanel("bio"),
        StreamFieldPanel("body", classname="full"),
    ]

#The user detail page
class UserDetailPage(Page):
    templates = "home/user_detail_page.html"
    photo_details = models.ForeignKey(
        "wagtailimages.Image",
        null=True,  #Home page is already exist
        blank=True, # it can not be blank
        on_delete=models.SET_NULL,
        related_name="+"
    )
    body = StreamField([
        ('tag', blocks.RichTextBlock(
            label='Tag', 
            features=['h1', 'h2', 'h3', 'bold', 'italic', 'link', 'hr'],
            default='I am a Software developer',
        )),
        ('comment', blocks.RichTextBlock(
            label='Comment', 
            features=['h1', 'h2', 'h3', 'bold', 'italic', 'link', 'hr'],
            default='I am fun',
        )),
        ('like', blocks.RichTextBlock(
            label='Like', 
            features=['h1', 'h2', 'h3', 'bold', 'italic', 'link', 'hr'],
            default='I like your comment',
        )),
    ], verbose_name='Contenu')

    content_panels = Page.content_panels + [
        ImageChooserPanel("photo_details"),
        StreamFieldPanel('body', classname="full"),
    ]

#The user feed page
class UserFeedPage(Page):
    templates = "home/user_feed_page.html"
    body = StreamField([
        ('user_photo', ImageChooserBlock(required=False))
    ], verbose_name='Contenu')
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]
    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]

class AlbumPage(Page):
    templates = "home/album_page.html"
    body = StreamField([
        ('description', blocks.RichTextBlock(
            label='Description',
            features=['h1', 'h2', 'h3', 'bold', 'italic', 'link', 'hr'],
            default="First album",
        )),
        ('photo_album', ImageChooserBlock(required=False)),
    ], verbose_name='Contenu')

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]

class PhotoPage(Page):
    templates = "home/photo_page.html"
    body = StreamField([
        ('photo_page', ImageChooserBlock(required=False)),
    ], verbose_name='Contenu')

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]

class Meta:
    verbose_name = "Home Page"
    verbose_name_plural = "Home Pages"