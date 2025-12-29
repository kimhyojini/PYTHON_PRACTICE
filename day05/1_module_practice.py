#카운트 다운이 있는 로또 번호 추첨기 만들기 

import random #import는 가지고 온다는 의미이다.
import time

#1.5초 카운트다운
for i in range(5,0,-1): #시간이 일초씩 지연되면서 5번 나올것임  #range:5초 동안 동안  -1을 붙이는 이유는 내림차순! 5에서 0까지 -1 
    print(f"{i}초 남았습니다.")
    time.sleep(1)
    
#2.로또번호 6개 추첨
numbers = list(range(1,46)) #range는 어디에서 어디까지~ = 연수된 정수 목록
lotto = random.sample(numbers,6)

#3. 오름차순 정렬
lotto.sort()

print(lotto)

n =input("숫자를 입력하세요 : ")
# 예외처리를 통해, 프로그램이 정상종료되도록 처리할 수 있다.


