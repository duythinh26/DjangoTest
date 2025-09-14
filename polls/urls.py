from django.urls import path

from . import views

# add an app_name to help with namespacing
app_name = "polls"

urlpatterns = [
    # Create a URL pattern for the index view
    # The empty string "" represents the root URL of the app
    # views.index is the index function we defined in views.py
    # name="index" gives the URL pattern a name that can be used for reverse URL
    path("", views.IndexView.as_view(), name="index"), # ex: /polls/
    
    # the 'name' value as called by the {% url %} template tag
    path("<int:pk>/", views.DetailView.as_view(), name="detail"), # ex: /polls/5/
    
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"), # ex: /polls/5/results/
    
    path("<int:question_id>/vote/", views.vote, name="vote"), # ex: /polls/5/vote/
]