from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice #현재 views 와 같은 경로 모델으로부터 퀘션
from django.utils import timezone

def insert(request):
    return render(
        request, 'polls/insert.html',{}
    )



def free(request):
    return render(
        request, 'polls/freelancer.html', {}
    )

def index(request):
    if request.method == 'POST':
        new = request.POST['new']
        q = Question(question_text = new, pub_date = timezone.now())
        q.save()

    latest_question_list = Question.objects.order_by('-pub_date')[:10] #오리지널 리스트 아님. 장고의 쿼리 셋? 같은 거임.
    #list comprehension : [xxx for q in list]
    output = ', '.join([q.question_text for q in latest_question_list])

    return render(request, 'polls/index.html', {'latest_question_list':latest_question_list})
    #return HttpResponse(output)


def detail(request, question_id): # 질문 상세 페이지
    question = Question.objects.get(pk=question_id)
    #return HttpResponse("You're looking at question %s." % question_id)
    return render(
        request, 'polls/detail.html',
        {'question':question}
    )


def results(request, question_id): # 투표 결과 페이지
    
    results = Question.objects.get(pk=question_id)
    
    return render ( 
        request, 'polls/results.html',
        {'results':results}
    )


def vote(request, question_id): # 투표 페이지
    num = request.POST['choice']
    choice = Choice.objects.get(pk=num)
    vote = choice.votes + 1 # 투표수 1 증가
    choice.votes = vote
    choice.save()

    return HttpResponse("You're voting on question %s." % question_id)