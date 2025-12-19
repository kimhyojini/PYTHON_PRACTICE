# 연산 ->처리를 하기 위한 목적처리를 하기 위한 목적
# 1. 산술 연산자
print('==산술연산자==')
a = 5
b = 2

# 사칙연산
print(a + b)
print(a/b) # 2.5 -> float(int / int) =>float 사칙연산의 경우 나눗셈은 float로 나온다.

# 몫,나머지,제곱
# //, %, **
print( a // b)
print(a % b)
print(a ** b)

 # 수학적으로 할 수 없는 연산은 파이썬도 할 수 없다.


# 2. 복합 연산자
# a = a + b -> 너무 길다 
# 산술연산자 & 할당연산자를 함께(복합) 쓰는 연산
# +=, -=, *= 많이 쓰는건 이 3가지 정도

print(a)
a += 1
print(a)


# 3.비교연산자
# 대소비교
# 값과 값을 비교한다. -> True, False
# A와 B를 비교, 딱 두개만 비교


# 일치 여부 비교 
# == : 같다 
# != : 같지 않다.

print(a == b)
print(a != b)

c = '123'
d = '456'

print( c == d)
print( c > d)
# print (a > d)  #같은 자료형이 아니면, 대소 비교 어려움
print(a == d) #같은자료형이 아니여도, 일치비교는 할 수 있다.

# 4.논리연산자
print('==논리연산자==')
print(a,b,c,d)
# False로 해석될 수 있는 변수 e 작성
e =  False
e = 0
# e = 0.0
# e = ""

print(type(e))
print(bool(e))

print(a,b,c,d,e)
# 6 2 "123" "456" 0

# A and B : A,B 둘다 True여야 True
# A or B : A,B 둘중 하나라도  True면 True임
# not A : A가 False이면, True

print(a and b)
print(True or dkjflkajdlk) # True를 만나고, or 연산임을 안 순간 더이상 평가하지 않음

# 연산자 정리
# "처리"

# 1. 산술 연산자 (+,-,*,/,//,%,**)
# 2. 복합 연산자 (+= , -=, *= ...) 연산후 다시 그 자리에 놓을 때 유용함
# 3. 비교 연산자 (==, !=. < , >, >=, <=)
# 4. 논리 연산자 (and, or, not) 불린형으로 인식될 수 있는 무언가가 a와 b위치에 온다, 불린형으로 해석될 수 있는 무언가가 와야만 한다.

