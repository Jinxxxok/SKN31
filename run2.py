#run2.py

#모듈에 있는 일부 함수, 클래스, 변수를 import -> 이름으로 호출가능
from calc import plus as p, minus # calc의 plus, minus 두 함수를 사용

result1 = p(100, 200)
result2 = minus(200, 300)

print(result1, result2)

from my_package import greet as g

g.hello_eng()
g.hello_kor()

print(g.__version__)

from my_package.greet import hello_eng, hello_kor

hello_kor()
hello_eng()

import sys
sys.path.append(r'c:\temp\lib')
from new_package import new_module

new_module.test_func()