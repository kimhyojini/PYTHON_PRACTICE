# 3일차 복습

# 변수~함수까지 
# 비교하며, 설명

print("=변수와 값=")

# 변수와 값의 개념을 헷갈림
# 변수이름=식별자=리터럴 할당연산자(=)를 통해 값을 가진다


a = 10
# a -> 데이터를 가리키는 이름 (변수) -> 언제든지 다시 할당이 가능
# 10 -> 실제 데이터 (값)

a = 20
print(a) #위에 10으로 적어놨지만, 20으로 재할당이 가능하며 실행해보면 a는 20으로 나온다.
# 변수명을 값을 잘 나타낼 수 있도록 이름을 짓는 것이 좋음
# 예를들면, a보다는 age라고 명명하는것이 더 좋은 것처럼!

print('== 입력과 출력 ==')
# 입력 : input() 내장함수
    # 목적 외부로부터 값 받기(사용자가 터미널 상 입력)
    #
    
# name = input('이름을 입력해주세요')
# print(name)
# print(type(name)) 

print('2.출력')
# 출력 : print() 내장함수를 통해서 씀
    # 목적 : 내부 값(파이썬)을 외부(터미널 상)에서 확인하기 위함
    # 반환값 : 없음
numbers= [1,2,3,4,5]
# len(numbers) #내부에서만 확인 가능 -> 이렇게 적으면 안됨
print(len(numbers)) #이렇게 입력해야함 

# input :외부 -> 내부
# print :내부(토드) ->외부(터미널)

print('=연산자비교=')

# 산술 연산자 
    # 연산 대상 : 수치형

a = 10  #int
b = 5.0 #float
print(a+b)
#문자도 가능하나, 이경우 곱셈과 더하기를 통해서 이어 붙이기이다.
# a = 'hello'
# b = 5.0
# print(a*b)  #선생님은 이어붙이기 나오던데,,, 난안나오네?^^ 


# 복합 연산자 
    # 연산 대상 : 수치형 / 가끔 문자열, 리스트 (+,*)
    # 산술연산 이후, 재할당
    # 반환 대상 : 산술연산 이후, 그 자리에 재할당한 값
a = a+b
# 연산 축약
a += b


# 비교 연산자
    #연산 대상: 같은 선상에서 비교할 수 있는것들
    # 반환 값: True, False (bool 자료형)
    
# a <= b  a>=b의 형태 : a 비교연산자 b의 형태
    #대소비교 : <, >=, >, <=
    #일치비교 : =, =!
print(a < b)

c = '오늘은'
d = '12/24'

print(a == b)
print(c >d) #순서가 있기 때문에, 숫자와 문자도 대소 비교는 가능하나, (1과 5순서등..) 직관적이지 않을 수 있음


# 논리 연산자
    # 연산 대상: 불린형의 무언가 / 논리값 (True, False)
    # 반환값: True, False라는 논리를 반환함 
    
# a 논리연산자 b 
# a and b
# a or b
# not a -> 이렇게 3종류 있는게 논리 연산자

print(True and False)

# 비교 연산과 함께 사용되는 경우 많음 
condition1 = a == b
condition2 = c != d

print(a == b and c != d)
print(condition1 and condition2) #이렇게 표현할 수도 있음 위에것과 같은 것임 

# 논리연산의 단축평가 
age = 20
print(age == 100 and djflkjasdfkjslk) #뒤에는 상관없이 False가 나옴, 왜냐하면 age는 20이니까!
# False and 정의되지 않은 변수 
# -> 필요이상의 연산 X, 바로 거짓 반환

print('=====조건문과 반복문=====')

# 조건문
    # 핵심 질문 : 특정 조건이 맞는가?
    # 실행 횟수 : 딱 1번
    # 판단 기준 : 논리 조건 (True, False)


score = 30

print('~조건문 시작~')
if score >= 60:
    print('합격')
elif score >= 50:
    print('예비합격')
else:
    print('불합격')
print('~ 조건문 끝~')

# 반복문 
    # 핵심 질문 :  몇 번 반복할 것인가?
    # 실행 횟수 :  여러번
    # 판단 기준 : 데이터의 갯수(for 문), 조건(while 문)
scores = [70,20,50,90,10]

print('~ 반복문 시작 ~')
for score in scores:
    print(score)
print('~반복문 끝~')

# 조건문=판단, 반복문=처리량

# 조건문 + 반복문 = 강력한 코드
scores = [70,20,50,90,10]

for score in scores:
    if score >= 60:
        print('합격')
    elif score >= 50:
        print('예비합격')
    else:
        print('불합격')
        
# 반복문의 종류
# 언제 무엇을 사용해야 하는가?

# for문 : 반복 횟수가 정해진 반복문
# while문 : 반복 횟수가 정해지지 않은 반복문

# for문 
    # 사용 기준 : 반복 횟수가 명확할때 사용
    # 사용처 :  컨테이너 자료형의 순회 (리스트, 딕셔너리, 문자열, range ...)
    # 안정성 : 높음
    
for i in range (5) : #정수목록
    print(i)
    
# while문
    # 사용기준: 종료 조건이 좀더 중요
    # 사용처: 상태 변화 추적하면서 반복해야만 할때 
    # 안정성: 낮음(주의!) -> 무한 루프 가능성 존재


number = 1
while number < 5:
    # print(number) #while문을 변경시킬 수 있는 코드를 print에 적지 않았기 때문에 무한으로 루프가 생성됨 -> ctrl+c로 나와야함
    number += 1 #조건에 대한 증감식
    

# print('=====컨테이너의 자료형 비교=====')
# 자료형	핵심 목적	순서	중복	수정	접근 방식	대표 사용 상황
# 리스트	여러 값을 순서대로 관리	O	O	O	인덱스	데이터 행, 시계열, 반복 처리
# 튜플	변하지 않는 묶음	O	O	X	인덱스	좌표, 설정값, 함수 반환
# 집합	중복 제거 & 포함 여부 판단	X	X	O	포함 여부	중복 제거, 교집합/차집합
# 딕셔너리	이름-값 매핑	X (3.7+ 입력순서 유지)	키 X	O	키	데이터 레코드, JSON

# 1.리스트 튜플
#리스트 [] 
    #핵심 목적: 여러 값을 순서대로 관리
    # 순서 : 존재함 ㅇㅇ
    # 수정 : 가능  #누군가는 이 자료를 바꿀 수 있음
    # 접근 방식 : 인덱스 [위치기반]

numbers = [1,2,3,4,5,6,6,6,6,6,6,6]
print(numbers)
numbers[0]=10


# 튜플 ()
    #핵심목적: 변하지 않는 묶음 
    # 순서: 0
    # 수정: x
    # 중복 :o
    # 접근 방식: 인덱스(위치기반)
    
numbers = (1,2,3,3)
print(numbers)

print(numbers[0])
# numbers[0] = 10 #TypeError

# 집합 {}
    # 핵심목적 : 중복이 되지 않음 xx
    # 순서 : x존재하지 않음
    # 수정: 가능가능! o
    # 접근 방식: 인덱스로 불가능, 포함 여부 확인 가능(멤버십 연산자) 

numbers = {1,2,3,4,5}
print(numbers) 

# numbers[0]  #TypeError: 'set' object is not subscriptable라고 뜨면서, 순서를 제공하지 않음을 보여줌 

print(1 in numbers)
numbers.add(10000) #순서가 없고, add를 한다고 해서 가장 뒤에온다거나 앞에온다거나 하는것이 보장되지 않음
print(numbers) 

# 딕셔너리 {}
    # 사용목적:  키-값 매핑하여 사용
    # 순서: 엄밀하게 X (단, 파이썬 3.7이상인 경우에는 입력순서를 유지하는 경향성이 있긴함)
    # 수정: 가능함 O
    # 중복: X 키가 중복되지 않는다.
    # 접근방식: key

user = {'name':'jun','age':30,'is_male' : True}


user['city'] = 'seoul' #수정이 가능하기 때문에, 위에 적혀있는거 외에 서울이 key값에 추가됨
user['city'] = 'busan' #중복은 불가능하고, 재할당이 되게됨 ->서울은 사라지도 부산만 나오는것임
user['lisense'] = True #값은 중복 가능, 같을 수 있음 true가 두번나오듯이, 키가 다르니까 상관없는것임

print(user)

for k in user. keys():
    print(user[k])
    
# 리스트 [] vs 튜플 ()
point = [10,20,30]
point[0] = 99 #가능
print(point)

# 튜플ㅣ 실수방지 -> 이건 바뀌면 안된다는 신호
#point = (10,20,30)
#point[0] = 99 #TypeError: 'tuple' object does not support item assignment이렇게 나옴 불가능

# 리스트 [] vs 집합 {}
# 의문점: 리스트를 그냥 사용하고, 중복만 없으면 되는거 아닌가요?

#리스트는 데이터 보관을 목적으로 한다.
names = ['A','B','C','D','A','C']
print(names)

#집합은 조건 판단 도구로 활용
names_set= set(names)
print(names_set)
print(len(names_set))
# => 방문자 여러번 방문 len을 통해 교집합등을 정리해야함 6명이 아니라 겹치는걸 제외하고 4명이 되는것임  
# => DAU 등 유저 한명이 두번접속했다고해서 , 두명으로 잡히지 않도록 이럴때 집합을 활용하는 것임

# 리스트 [] VS딕셔너리 {key:value}
#리스트: 순서를 알아야 의미가 있음
user = ['jun',25,'개발자',True]
print(user)

#딕셔너리: 의미가 코드에 그대로 드러남,더 많은 부연설명을 할 필요가 없음 
user = {'name':'jun',
        'age':25,
        'occupation':'개발자',
        'live_seoul': True}
print(user)

#['jun', 25, '개발자', True]
#{'name': 'jun', 'age': 25, 'occupation': '개발자', 'live_seoul': True} 이렇게 각각 결과값이 나오는 것임!!

# 반복문 +컨테이너
numbers = [1,2,3,4,5]  #얘는 1,2,3여기를 보여줌 
for variable in numbers:
    print(variable)
    
user = {'name':'jun',  #딕셔너리의 경우 똑같은 형태처럼 보이지만, 키값만 보여준다 ->key만 할당
        'age':25,
        'occupation':'개발자',
        'live_seoul': True}
for variable in user:
    print(variable)   
    
for k,v in user.items(): #각각 키와밸류 모두를 꺼내고 싶으면 이 수식을 사용해야 한다.-> 한쌍을 그대로 
    print(k,v)

tags = ['python','data','bi','sql']  #집합: 집합적 성격을 띄고 있기에, 중복하려고 해도 중복은 안된다.
print(tags)

tags.add('python')
print(tags)

for tag in tags:
    print(tag)