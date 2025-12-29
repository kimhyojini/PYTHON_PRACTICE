# [실습 6] 
# 전체 출석부와 현재 출석한 인원이 리스트로 주어질 때, 출석하지 않은 인원을 출력하시오. (순서 굳이 상관 없음)
students = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # 전체 명단
attened = ['c', 'e', 'f', 'h']  # 출석 명단
absent = []
#내가적은답안
# print[not attened]

#내가 다시 구성한 답안
for student in students:
    if student not in attened:
        absent.append(student)
    #“지금 검사 중인 학생(student)을 결석자 리스트(absent)의 맨 뒤에 추가해라”

print(absent)

#원래 답안
for student in students:
    if student not in attened:
        print(student)