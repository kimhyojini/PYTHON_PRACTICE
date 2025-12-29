# 내장함수
# 파이썬 자체적으로 제공하는 함수 

numbers = [1,2,3,4,5]
print(len(numbers))

word = 'hello python!'
print(len(word)) #문자열도 숫자세어서 13자라고 알려줌

is_male = True
#print(len(is_male))  #TypeError: object of type 'bool' has no len()라고 뜸
#컨테이너 자료형의 item 갯수를 세어 반환
#길이를 반환한다.


#사용자 정의함수 len_func 작성
numbers = [1,2,3,4,5,45,66,75,23,400]
#1단계: 정의 

def len_func(container):
    answer = 0 #값을 세어내기 위한 초기값 설정 
    for item in container:
        answer += 1
    return answer

print(len_func(numbers))
#2단계: 호출

# 내장함수 sum()
print(sum(numbers))

def sum_func(container):
    answer=0
    for item in container:
        answer += item
    return answer

print(sum_func(numbers))

# sorted

# users = {
#     'name': ['jun','alex','chelsea']
#     'age':[21]} 


#내장함수 
#컨테이너자료형의 각원소에 함소를 적용한 후, 그 결과를 반환
number_str = '12345'
number_lst = list(number_str)
numbers = []
for n in number_lst:
    numbers.append(int(n))
print(numbers)

map(int,number_str)

#방법2
numbers = list(map(int,number_str))
print(numbers)
# => 대안이 있다면 , 더편한 방식선택해서 할것 햣 
