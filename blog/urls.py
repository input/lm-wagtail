from django.urls import path

from .views import BlogAtom, BlogRSS


urlpatterns = [
    path('blog/atom/', BlogAtom()),
    path('blog/rss/', BlogRSS()),
]
