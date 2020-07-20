from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.http import request, HttpResponse

from django.http import HttpResponse
import os
def upload1(request):
 if request.method == 'GET':
     return render(request, 'file/upload1.html', {})
 else:
     upload_file = request.FILES['my_file']
     try: # 디렉토리 생성
         os.mkdir('upload1')
     except FileExistsError as e:
         pass
     file_name = upload_file.name
     with open('upload1/' + file_name, 'wb') as file:
         for chunk in upload_file.chunks():
             file.write(chunk)
     return HttpResponse('파일 업로드 완료')

def index2(request):
    return render(request, 'polls/index2.html',{})
def index (request):
    q_list= Question.objects.order_by('pub_date')[:5]# -pub_date 라고 하면 역순

#    str_list=[q.question_text for q in q_list]
#    html =','.join(str_list)
     
    # return HttpResponse(html)
    return render(request, 'polls/index.html',{'latest_question_list':q_list})

def detail(request, question_id):  # 질문 상세 페이지
    question = Question.objects.get(id=question_id)
    return render(request, 'polls/detail.html',{'question':question})
   # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):  # 투표 결과 페이지
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def reset(request, question_id):
    question = Question.objects.get(id=question_id)
    choice_list = question.choice_set.all()
    for choice in choice_list:
        choice.votes = 0
        choice.save()

    return HttpResponse('OK')



def vote(request, question_id):  # 투표 페이지
    # request.POST['choice']
    choice_id = request.POST.get('choice') 

    #질문 조회
    question = Question.objects.get(id=question_id)
    #보기 조회
    choice = question.choice_set.get(id=choice_id)
    #투표수 증가
    choice.votes +=1
    #저장
    choice.save()

    #return HttpResponse("You're voting on question %s." % question_id)
    return HttpResponseRedirect('/polls/%s/' % question_id) # 변수 출처확인!!
    #return HttpResponseRedirect(reverse('detail',args=(question_id)))


def logout(request):
    request.session.clear()

    return HttpResponse('로그아웃')



def login(request):

    return render(request, 'polls/login.html')

def login_post(request):
    user_id = request.GET.get('user_id')
    user_pw = request.GET.get('user_pw')
    print(user_id,user_pw)
    request.session['user_id'] = user_id

    return HttpResponse("로그인 완료")


def download(request):
 filepath = os.path.join(settings.BASE_DIR, 'upload/파일명.txt')
 filename = os.path.basename(filepath)
 with open(filepath, 'rb') as f:
 response = HttpResponse(f, content_type='text/html')
 response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
 return response
