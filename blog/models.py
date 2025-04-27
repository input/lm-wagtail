from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageBlock
from wagtail.models import Page
from wagtail.search import index

from base.models import CodeBlock


class BlogIndexPage(Page):
    """The 'Blog' index page (/blog). A `title` field is added by Wagtail."""
    intro = RichTextField(
        blank=True,
        null=False
    )

    def get_context(self, request):
        # Add `blog_pages`, which comprises published posts in reverse
        # chronological order.
        context = super().get_context(request)
        blog_pages = self.get_children().live().order_by('-first_published_at')
        context['blog_pages'] = blog_pages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPage(Page):
    """The `Blog` page type. A `title` field is added by Wagtail."""
    date = models.DateField(
        "Post date"
    )
    summary = RichTextField(
        blank=True,
        null=False,
        features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'strikethrough', 'blockquote'],
        help_text="A summary of the post, which will be displayed on the blog index page."
    )
    body = StreamField([
        ('text', RichTextBlock(
            features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'strikethrough', 'blockquote']
        )),
        ('image', ImageBlock()),
        ('code', CodeBlock()),
    ])
    tags = ClusterTaggableManager(
        through=BlogPageTag,
        blank=True
    )

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('summary'),
        FieldPanel('body'),
        FieldPanel('tags'),
    ]

    def get_absolute_url(self):
        return "/blog/%s/" % (self.slug)


class BlogTagIndexPage(Page):
    """A blog tag index page (for example, /tags/?tag=django)."""
    def get_context(self, request):
        # Add `blog_pages`, which comprises published posts in reverse
        # chronological order, filtered by the requested tag.
        context = super().get_context(request)
        tag = request.GET.get('tag')
        blog_pages = BlogPage.objects.filter(tags__name=tag).live().order_by('-first_published_at')
        context['blog_pages'] = blog_pages
        return context
