from multiprocessing import context
import re
from urllib import response
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from polls.models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context ={'latest_question_list': latest_question_list}
    # render 函数的作用：「载入模板，填充上下文，再返回由它生成的 HttpResponse 对象」
    return render(request, 'polls/index.html', context)

    # version-03
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # version-02: 
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # version-01: 
    # return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # version-02
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    # version-01
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
