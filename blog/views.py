import datetime
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.utils.html import strip_tags
from blog.models import BlogPage


class BlogRSS(Feed):
    """RSS feed for the whole blog (/blog/rss)"""
    title = "Laurence Mercer's Blog"
    link = "/blog/"
    description = "Posts about Python, Django, and Wagtail development."

    def items(self):
        return BlogPage.objects.live().order_by("-date")[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return strip_tags(item.summary)

    def item_pubdate(self, item):
        return datetime.datetime(item.date.year, item.date.month, item.date.day)


class BlogAtom(BlogRSS):
    """Atom feed for the whole blog (/blog/atom)"""
    feed_type = Atom1Feed
    subtitle = BlogRSS.description
