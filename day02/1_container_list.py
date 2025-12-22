# 컨테이너 자료형
# # 리스트 (list)
# 연속되어 있는, 순서가 존재하는, 가변 자료형
# 0개 이상의 값을 순서 있게 저장하는 자료형

numbers = [10,20,30,40,50]
print(numbers)
print(type(numbers))

# 비어있는 리스트도 리스트다.
empty = []
print(empty)
print(type(empty))

#리스트 연산
# + 연산 : 리스트끼리 연결
# 리스트 + 리스트 
number_1 = [1,2]
number_2 = [3,4]
number_3 = number_1+number_2

print(number_3)

print(id(number_1))
print(id(number_2))
print(id(number_3))

# => 연산의 결과, 새로운 리스트를 생성

# * 연산 : 같은 리스트를 n번 반복하여 합쳐서 "새로운 리스트" 생성
# 리스트 * 반복 횟수(int) 여야만 한다.

print(number_1)
# print(number_1 * number_2) #에러발생

print('=====리스트의 특징=====')
# 특징1. 순서가 있는 자료형


# 인덱싱 = 인덱스(index)라고 하는 위치를 기준으로 원소에 접근
# 리스트[인덱스] -> 인덱스 위치에 원소를 확인 

# 인덱스 0 부터 시작 
numbers =[10,20,30,40,50]

# 인덱스 0,1,2,3,4 (0부터 시작하여, n-1번까지 존재)
# 음수 인덱싱 -5,-4,-3,-2,-1 (-1가 가장 마지막 원소)

print(numbers[0])
print(numbers[2])

print(numbers[-1])

print('==슬라이싱==')
#리스트 [시작:끝:간격]을 나타내는 숫자 
print(numbers[1:3])
print(numbers[5:2:-1])

# 리스트 뒤집기
print(numbers[: : -1])