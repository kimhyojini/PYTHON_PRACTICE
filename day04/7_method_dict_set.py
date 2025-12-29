# 값 조회 


# 값 조회 : get 
# key를 기준으로 value를 가지고 옵니다.
# 만약 값이 없으면, 반환할 값이 없다는 None을 나타냅니다.

students = {'jun':40,
            'alex':20,
            'kyle':30,
            'ken':22}
print(students.get('ken'))
print(students.get('beny'))

print(students.get('beny','key가 존재하지 않습니다'))

#수정 
students.update({'jun':300})
print(students)

#추가
students.update({'chelsea':30})
print(students)

#삭제 
#전달된 키에 해당하는 한쌍을 삭제 
# 실제 삭제되는 값을 보지 못하므로, 반환->삭제되는 값을 반환 
students.pop('alex')
print(students)

deleted_student = students.pop('alex')
print(deleted_student)
print(students)

deleted_student = students.pop('heater')

# 집합(set)
    # 순서: x
    # 수정: o
    # 중복: x

numbers_1 = {1,3,5,7,9}
numbers_2 = {1,2,3,4,5}

# 집합 연산
print(numbers_1.intersection(numbers_2)) #교집합
print(numbers_1.difference(numbers_2)) #차집합
print(numbers_1.solution)

print(numbers_1) #중복을 허락하지 않음
numbers_1.remove(10000)
print(numbers_1)
#삭제 


#여러 값 추가 : update(
#

numbers_1.update([10,20,30])
print(numbers_1)