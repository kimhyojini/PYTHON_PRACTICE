# 모듈
#함수의 정의와 호출을 분리하기 위한 목적
 
# 기본 사용법
# import 모듈 -> 모듈을 불러와서 사용할 수 있다.
import module_A 

#호출
print(module_A.add(1,2))  #여기에서 호출이 일어나서 3이라는 값이 나옴

print(module_A.subtract(1,10000)) #호출

#일부만 불러오고 싶을때는?
from module_A import subtract
from module_A import * #함수를 다 불러올 수도 있음


#  함수 이름이 너무 길때?
from module_A import subject as ab

print(sb(1,10000))