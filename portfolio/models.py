from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page


class PortfolioIndexPage(Page):
    """
    The 'Portfolio' index page (/portfolio).
    A `title` field is added by Wagtail.
    """
    intro = RichTextField(
        blank=True,
        null=False
    )
    further_projects = RichTextField(
        blank=True,
        null=False
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('featured_projects', label="Featured projects"),
        FieldPanel('further_projects'),
    ]


class PortfolioPage(Page):
    """The `Portfolio` page type. A `title` field is added by Wagtail."""
    client = models.CharField(
        max_length=255,
        blank=True,
        null=False,
        help_text="The client of the project."
    )
    role = models.CharField(
        max_length=255,
        blank=True,
        null=False,
        help_text="My role in the project."
    )
    stack = models.CharField(
        max_length=255,
        blank=True,
        null=False,
        help_text="The stack used for the project."
    )
    summary = RichTextField(
        blank=True,
        null=False,
        help_text="A brief description of the project, which will be displayed on the portfolio index page."
    )
    description = RichTextField(
        blank=True,
        null=False,
        help_text="A full description of the project, which will be displayed on an individual project page."
    )

    def main_image(self):
        project_image = self.project_images.first()
        if project_image:
            return project_image.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('client'),
        FieldPanel('role'),
        FieldPanel('stack'),
        FieldPanel('summary'),
        FieldPanel('description'),
        InlinePanel('project_links', label="Links"),
        InlinePanel('project_images', label="Images"),
    ]


class FeaturedProject(Orderable):
    """A project which is featured on the portfolio index page."""
    page = ParentalKey(
        'portfolio.PortfolioIndexPage',
        on_delete=models.CASCADE,
        related_name='featured_projects'
    )
    project = models.ForeignKey(
        'portfolio.PortfolioPage',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    panels = [
        FieldPanel('project'),
    ]


class ProjectImage(Orderable):
    """A single image (plus caption) of a project."""
    page = ParentalKey(
        'portfolio.PortfolioPage',
        on_delete=models.CASCADE,
        related_name='project_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = RichTextField(
        blank=True,
        null=False
    )

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


class ProjectLink(Orderable):
    """A project-related link. For example, to a production website."""
    page = ParentalKey(
        'portfolio.PortfolioPage',
        on_delete=models.CASCADE,
        related_name='project_links'
    )
    text = models.CharField(
        max_length=255,
        blank=True,
        null=False,
        help_text="The text to display."
    )
    url = models.URLField(
        blank=True,
        null=False
    )

    panels = [
        FieldPanel('text'),
        FieldPanel('url'),
    ]
