from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# 모델 클래스 import
from .models import Question, Choice


# View 함수 정의 - URL Conf에 등록(url mapping)
## URL Conf: 요청URL과 View함수를 mapping 하는 파일.
## config/settings.py -> ROOT_URLCONF에 설정된 파일.

# 설문 웰컴 페이지 응답하는 View함수
def welcome_polls(request):
    now = datetime.now() # 실행시점 일시
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")

    # 응답 페이지를 생성
    res_html = """<!doctype html>
<html>
    <head>
        <title>Polls - Welcome</title>
    </head>
    <body>
        <h1>Welcome></h1>
        <p>저희 설문 페이지에 방문해 주셔서 감사합니다.</p>
        현재 시간: {now_str}
    </body>
</html>
"""
    print("Polls/welcome 실행")
    return HttpResponse(res_html)

def welcome_polls(request):
    now = datetime.now() # 실행시점 일시
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    # 응답 -> poll/welcome.html 템플릿 호출 -> html string으로 호출
    ## template을 호출하는 함수 -> render()
    res_html = render(
        request, # request
        "polls/welcome.html", # 템플릿 파일 경로(app\templates 빼고 나머지 경로)
        {"now":now_str} # context-value를 dictionary로 설정. -> View가 Template에게 전달하는 값(객체)
    )
    print(res_html) # HttpResponse
    return res_html

######################################################################
# 설문 목록 조회
## 전체 question들을 조회해서 목록으로 출력
## 요청 url: polls\list
## View 함수: vote_list
## template: polls\vote_list.html
######################################################################
# View함수 파라미터: 1 - request: HttpRequest 객체(HTTP 요청정보)를 받는 변수(필수!)
#                    2 - path 파라미터를 받기 위한 변수들(옵션, 필수아님)
def vote_list(request):
    # DB에서 Question들을 조회
    question_list = Question.objects.all().order_by("-pub_date")

    # 응답화면 - Context Value로 question_list를 전달.
    return render(
        request, "polls/vote_list.html", {"question_list": question_list}
    )
