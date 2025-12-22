# 커피 구매와 거스름돈 계산 프로그램

# money = int(input('현재 잔액을 입력해 주세요')) # 현재 보유 금액

# 코드 입력

# price = 2000

# 몫을 나타내는 연산자 : //
# count = money // price #커피구매
# 나머지를 나타내는 연산자 : %
# change = money % price #거스름돈



# print(count)
# print(change)

# 2.버스 요금 계산
    #나이(age)와 결제 수단(card_type: "일반" 또는 "정기권")을 입력받아 버스요금을 출력하세요.
    #정기권이면 무조건 0원
    #정기권이 아니면 기존 나이 규칙 적용
    #7세 미만 또는 65세 이상: "무료"
    #7세 이상 19세 이하: "청소년 요금"
    #20세 이상 64세 이하: "성인 요금"

## 2. 버스 요금 계산

# age = int(input('나이를 입력해 주세요.'))
# card_type = input('결제 수단을 입력해 주세요 :')

# if card_type == '정기권':
#     print('0원')
# elif age < 7 or age >= 65 :
#     print('무료')
# elif age <=19 :
#     print('청소년 요금')
# else : 
#     print('성인 요금')

# 리스트의 특징 2: 가변 자료형
# 가능하다 ,변경이 -> 수정, 삭제, 추가 가능
# 객체 자체를 바꾸지 않고도 변경가능

# 2. 추가 
# 리스트의 가장 마지막 위치에 추가 

# numbers[5] = 60 # 에러발생
# numbers.append(60)
# print(numbers)

# 3.삭제
# numbers.pop() #가장 마지막 요소 삭제
# print(numbers)
# print(id(numbers))

#자료형 자체를 변경하더라도, 주소값에 영향이 없다.

# 듀플

# 1. 순서가 존재하는 자료형
# 2. 불변 자료형

# 듀플 생성(값, 값, 값)
numbers = (10,20,30,40,50)
print(numbers)
print(type(numbers))


# 연산 가능 (+,*)
# 연산 후에는 새로운 튜플을 만들어 낸다.
numbers_1 = (1,2)
numbers_2 = (3,4)
numbers_3 = numbers_1 + numbers_2
print(numbers_1+numbers_2)

# 튜플의 특징 2: 불변자료형 (immutable)
# 불가능하다. 변경이 

# 수정 
# numbers[1] = -1 #TypeError: 'tuple' object does not support item assignment이라고 나오면서 안됨

#추가
numbers.append(60)

