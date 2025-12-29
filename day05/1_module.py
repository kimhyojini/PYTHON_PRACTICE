# 모듈
#함수의 정의와 호출을 분리하기 위한 목적
 
# 기본 사용법
# import 모듈 -> 모듈을 불러와서 사용할 수 있다.
import module_A 

#호출
print(module_A.add(1,2))  #여기에서 호출이 일어나서 3이라는 값이 나옴

print(module_A.subtract(1,10000)) #호출

print(module_A.add(1,2))
#일부만 불러오고 싶을때는?
from module_A import subtract
from module_A import * #함수를 다 불러올 수도 있음


#  함수 이름이 너무 길때?
#from module_A import subject as ab

#(sb(1,10000))

#주어진 리스트내 무작위 1개 추출

#random이라고 하는 너셕을 통해서 정수값을 뽑을수도 있고, 십 이십 삼십 사십 오십 정수값이 아닐지라도 랜덤은 추출이 가능하다 

#random.shuffle

import time


print(time.time())
time.sleep(3)
print('3초가 지났습니다')

# 반복이 너무 빠르게 흘러가며 안될때 쓰임

#예
for i in range(5):
    time.sleep(1)
    print(f'1초 기다린 후, {i}출력')

