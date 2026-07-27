# polls/urls.py
## polls app의 url conf 파일. (app별로 url 설정을 따로하기.)

## urlconf: urlpatterns = []를 가지고 있어야 한다.
## Root UrlConf에 등록 (설정)

from django.urls import path
from . import views

app_name = "polls" # urls.py를 App별로 만들때 식별하기 위한 이름.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'))
    # polls: rul이 polls로 시작하면 나머지는 polls/ urls.py를 참조하라.
]



urlpatterns = [
    path('admin/', admin.site.urls),
    # 파라미터 1: url, 2: 함수, name="설정이름"
    path('polls/welcome', views.welcome_polls, name="polls_welcome"),
    # http://127.0.0.1:8000/polls/welcome -> welcome_polls()
]
