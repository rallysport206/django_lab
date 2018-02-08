from django.conf.urls import url
from mypolls import views

urlpatterns = [
    # Matches /polls/
    url(r'^$', views.index, name='index'),
    # Matches /polls/5/votes
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ^how we get question out of db
    # Match /polls/5/results
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # Match /polls/5/vote/results
    url(r'^(?P<question_id>[0-9]+)/vote/process$', views.process_vote, name='process_vote'),
]
