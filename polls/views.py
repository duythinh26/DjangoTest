# Views used to handle web pages and other content
# Each view is represented by a Python function
# To get from a URL to a view, Django uses what are known as ‘URLconfs’. A URLconf maps URL patterns to views.

from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from polls.models import Question


# Each view function takes at least one argument, typically a request argument.
# Each view is responsible for doing one of two things: returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404
def index(request):
    # .order_by("-pub_date"): Sort questions by posting date, minus sign (-) means from newest to oldest.
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    
    #Create a "context" - this is a dictionary to pass data from the view to the template.
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)