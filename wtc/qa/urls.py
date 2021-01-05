from django.urls import path
from django.conf import settings

from django.urls import path, include

# from qa.views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:qid>/<slug:qslug>', views.viewquestion, name='viewquestion'),
    path('ask-question', views.askquestion, name='askquestion'),
    path('ajax-answer-question', views.ajaxanswerquestion, name='ajaxanswerquestion'),
    # path('', index),
    # path('question/<int:qid>/<slug:qslug>', viewquestion),
    # path('ask-question', askquestion),
    # path('ajax-answer-question', ajaxanswerquestion)
]