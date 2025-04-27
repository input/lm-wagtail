from wagtail.admin.panels import FieldPanel
from wagtail.blocks import CharBlock, ChoiceBlock, RichTextBlock, StructBlock, TextBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageBlock
from wagtail.models import Page


class BasicPage(Page):
    """The `Basic` page type. A `title` field is added by Wagtail."""
    intro = RichTextField(
        blank=True,
        null=False,
    )
    features_custom=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'strikethrough', 'blockquote']
    body = StreamField([
        ('text', RichTextBlock(
            features=features_custom
        )),
        ('text_2_column', StructBlock(
            [
                ('column_1', RichTextBlock(
                    features=features_custom
                )),
                ('column_2', RichTextBlock(
                    features=features_custom
                )),
            ],
            template='base/text_2_column_block.html',
        )),
        ('image', ImageBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]


class CodeBlock(StructBlock):
    """
    A custom Wagtail Streamfield block for displaying code highlighted using
    highlight.js.
    @see https://github.com/highlightjs/highlight.js/
    """
    language = ChoiceBlock(
        choices=[
            ("bash", "Bash"),
            ("cs", "C#"),
            ("css", "CSS"),
            ("django", "Django"),
            ("dockerfile", "Dockerfile"),
            ("gdscript", "GDScript"),
            ("graphql", "GraphQL"),
            ("javascript", "JavaScript"),
            ("json", "JSON"),
            ("html", "HTML"),
            ("tex", "LaTeX"),
            ("less", "Less"),
            ("markdown", "Markdown"),
            ("nginx", "Nginx"),
            ("plaintext", "Plaintext"),
            ("postgresql", "PostgreSQL"),
            ("php", "PHP"),
            ("python", "Python"),
            ("python-repl", "Python REPL"),
            ("scss", "SCSS"),
            ("sql", "SQL"),
            ("twig", "Twig"),
            ("typescript", "TypeScript"),
            ("xml", "XML"),
            ("yml", "YAML"),
        ],
        required=False
    )
    filename = CharBlock(
        required=False
    )
    code = TextBlock(
        form_classname="code-block",
        rows=5
    )

    class Meta:
        template = "base/code_block.html"
