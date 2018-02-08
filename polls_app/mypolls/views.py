from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import F
from .models import Question, Choice

def index(request):
    # return HttpResponse('youre at the index page')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'mypolls/index.html', { 'latest_question_list': latest_question_list })

def vote(request, question_id):
    # return HttpResponse('youre at the vote page!')
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'mypolls/vote.html', {'question': q })

def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'mypolls/results.html', {'question': q })

def process_vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'mypolls/vote.html', { 'question': q, 'error_message': 'you need to make a choice' })
    else:
        selected_choice.votes += F('votes') + 1
        selected_choice.save()
        return redirect(request, '/polls/{0}/results'.format(question_id))
