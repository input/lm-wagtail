from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(60*60*24)
def welcome(request):
    return HttpResponse('👋 Hello, world.')
