from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404

from django.template import loader
from .models import Question

def index(request):
    return HttpResponse('人气菜式争霸')


def details(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/details.html',{'question':question})


def results(request, question_id):
    response = "问题 %s 的答案"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('对问题 %s 投票' % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list
    }
    return HttpResponse(template.render(context,request))

