# 함수 기능
# 코드 재사용을 위한 블랙박스적인 블럭이다.
# 입력을 넣으면, 처리하고, 반환(=출력)한다.


#사용자 정의 함수
# 1단계: 선언(define)

def abs_num(n):
    if n > 0:
        answer = n
    else:
        answer = -1 * n
    return answer    
#이거 하고 돌려도 아무런 정의가 나오지 않음 
#return이라는 키워드 만나게 되면 함수는 종료됨(output이 나오면 다시 계산에 들어갈 수 없음)


# 2단계 : 호출(call)

i = -123
result= abs_num(i) # -123은 인자 
print(result)

#내장함수
numbers = [1,2,3,4,5,6]
print(len(numbers)) #컨테이너의 길이를 반환하는 내장함수
print(abs(-100)) #절댓값을 알아보는 함수? 
print(sum(numbers)) #다 더해달라는 함수 컨테이너의 합계를 반환하는 내장함수(이미 기능이 있는...)

def abs_num(n):
    if n > 0:
        return n
    else:
        return -1 * n  #위에것과 사실 똑같은 함수여서, 같은 결과값을 나타낸다. answer라는 변수를 따로 쓰지 않고 바로 반환한것임  
    return answer  