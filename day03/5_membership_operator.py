#  멤버십 연산자
# in / not in

# 특정 값이 컨테이너 자료형에 포함이 되어 있는지 검사 
numbers = [1,2,3,4,5]
print(type(numbers))

print(3 in numbers)
print(3 not in numbers)

# 질문
# print(3 in 3) #nt' is not iterable 이렇게 나옴 컨테이너 자료형일때만 멤버십이 가능함 

# 예시1. 3이 있는지를 확인하는 코드
for num in numbers:
    print(num)
    if num == 3:
        print('3이 있습니다.')
        break

# 예시2. 멤버십 연산자(좀더 간단한 코드로 사용할 수 있음) 그리고 in뒤에는 무조건 컨테이너형 자료형이 와야한다.
if 3 in numbers:
    print('3이 있습니다.')
    
# 딕셔너리와 멤버십 연산자
colors = {'Red':'빨강',
          'Blue': '파랑',
          'Yellow':'노랑'}

# 질문
print('빨강' in colors) #False 

print('Red' in colors) #True
# => key 모음에 포함될 때만 True라고 함

# values에서 존재여부를 검사하고 싶을 때,
# colors.valures() 메소드 사용하며 된다!
print(colors.valures())

print('빨강' in colors.values())