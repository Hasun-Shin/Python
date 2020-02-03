from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice #현재 views 와 같은 경로 모델으로부터 퀘션
from django.utils import timezone


# def new_choice(request):
#     return render(
#         request, 'polls/new_choice.html',{}
#     )


def new_choice(request):
    return render(
        request, 'polls/new_choice.html',{}
    )



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
        # new = request.POST['new']
        new = request.POST.get('new')
        answer1 = request.POST.get('answer1')
        answer2 = request.POST.get('answer2')

        # answer_list = request.POST.getlist('answer')

        q = Question(question_text = new, pub_date = timezone.now())
        q.save()

        #보기 1번 입력 방식 
        q.choice_set.create(choice_text=answer1, votes=0)

        #보기 2번 입력 방식
        Choice(choice_text=answer2, votes=0, question=q).save()

    
    latest_question_list = Question.objects.order_by('pub_date')[:100] #오리지널 리스트 아님. 장고의 쿼리 셋? 같은 거임.
    # latest_question_list = Question.objects.order_by('-pub_date')[:100]
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

#@csrf.expt #데코레이터 csrf 코드를 이 함수에서는 활요하지 않음. 
#ajax 호출 시 주로 사용,  csrf 기능 무효화
def vote(request, question_id): # 투표 페이지
    num = request.POST['choice']
    choice = Choice.objects.get(pk=num)
    vote = choice.votes + 1 # 투표수 1 증가
    choice.votes = vote
    choice.save()

    return HttpResponse("You're voting on question %s." % question_id)

    #1번 방식.. 평범한 웹사이트 주소 호출
    return HttpResponse('<script>alert("완료");history.back()')

    #2번 방식 .. AJAX
    #                투표하는 화면(HTML)에서 ajax 코드 작성
    