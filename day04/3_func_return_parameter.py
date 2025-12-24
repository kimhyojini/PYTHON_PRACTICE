# 반환값과 매개변수 유무 

# 반환값 X, 매개변수 O
# 선언할때는 실행 X 동작하지 않음
def hello(name):
    print('함수 안에서 출력') #2
    print(f'안녕하세요! {name}님') #3
    
print('함수 밖에서 출력') #1
hello('jun') #4 -> hello 함수가 반환하는 것이 없기 때문에 None이 출력

# 매개변수와 반환값은 함수를 구성할때 필수 요소는 아니다.
# 즉, 없어도 함수를 정의할 수 있다.
# 원하는 설계에 따라 선택하여 사용하면 된다.

# 자연수 N을 입력받아, N줄까지 별을 출력하는 함수를 만드시오.
# 첫 번째 줄은 별이 1개이며, N번째 줄은 N개의 별이 찍혀야 합니다.

# ex) 만약 N이 3 이라면?
# *
# **
# ***

# N = int(input())

# def print_stars():
#     # pass를 지우고 로직을 작성합니다.
#     pass

N = int(input('정수를 입력해 주세요 :'))

#함수정의 
#매개변수는 숫자n으로 존재함(n번 반복함)
# 매개변수0, 반환값X

def print_stars(n):
    pass

def print_stars(N):
    for i in range(1, N+1) :
        print('*' * i)
  
print_stars(N)



