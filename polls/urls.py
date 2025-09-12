from django.urls import path

from . import views

urlpatterns = [
    # Create a URL pattern for the index view
    # The empty string "" represents the root URL of the app
    # views.index is the index function we defined in views.py
    # name="index" gives the URL pattern a name that can be used for reverse URL
    path("", views.index, name="index"),
]