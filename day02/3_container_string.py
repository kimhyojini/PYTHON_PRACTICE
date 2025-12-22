word = 'hello'
subject = 'python'
#문자열

#특징 1:순서가 존재한다.
#인덱스 위치로 값을 확인할 수 있음
#덧셈 연산
print(word+subject)

# => 문자열끼리 바로 이어 붙인다.

# * 연산 : 문자열 * 반복횟수(int)
# 특징 1: 순서가 존재한다.
# 인덱스(위치)로 값을 확인 가능
print(subject *3)
print(subject[-1])

# 특징2: 불변자료형(immutable)
# 불가능하다, 변경이

subject[0] = 'P'