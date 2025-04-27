from django.urls import path

from . import views

urlpatterns = [
    path('examples/welcome/', views.welcome)
]
