# 익명함수
# lambda
# 왜 이름이 없어? 이름 붙이는게 중요하지 않아서 

# 기존의 방식
# def add(x,y):
#     answer: 
#     return answer

# 익명함수를 이용한 방식
result = (lambda x,y: x + y)(1,4)
print(result)

numbers = [1,5,3,7,10,4]
print(numbers)

print(sorted(numbers, key=lambda x: -x))


#리스트 형태 
example = [(0,2),(3,5),(1,4),(0,-1)] #뒤에 있는 녀석을 기준으로 정렬하고 싶음 
# 각 요소 (앞, 뒤)라고 했을때, 뒤를 기준으로 오름차순 정렬을 하고싶을때.. 

example_new = sorted(example, key=lambda x:x[1])
print(example_new)

print(type(example))
