# 복습
# 다양한 자료를 이용하여, 정보를 구조화하는 방식이 알고리즘에서 중요하다.

# 복습 실습 
users = {
        'total_user': 3,
        'information': [
            {'name': 'alex', 'age':3, 'license':True},
            {'name': 'june', 'age':7, 'license':False},
            {'name': 'peter', 'age':4, 'license':False}
        ]
        }

# Q1. 라이센스가 있는 인원들의 숫자 구하기

count=0
for user in users['information']:
    if user['license'] == True:
        count += 1

print(f'라이센스가 있는 인원{count}명')
# Q2. 모든 사람의 나이 평균 구하기
total_age=0

for user in users['information']:
    total_age += user['age']

average_age = total_age / users['total_user']
print(average_age)
    
# Q3. 라이센스가 없는 사람들의 이름 모으기
no_license_name = []
for user in users['information']:
    if user['license'] == False:
        no_license_name.append(user['name'])

print(no_license_name)

# 1.사용자 정의 함수
# 1단계: 정의(define)

students = ['하늘','수빈','동연','강현','선준','예솔','하비','동호','채원','효진','세연']
# 학생 목록과 이름이 들어가면, 출석 여부를 반환하는 함수 
def check(students_list,name): #매개변수
    if name in students: # 멤버십 연산으로 포함 여부 확인
        return f'{name}님은 출석하셨습니다.'
    else:
        return f'{name}님은 출석하지 않으셨습니다.'

# 2단계: 호출하기
print(check(students,'채원'))

# 만약 고정된 학생 목록이 존재한다면, 매개변수로 빼지 않아도 됨 

# 다만 이경우에는
#print(check('하은')) #설계한대로 사용하지 않으면, 에러발생

# 2.내장함수
print(students) #터미널 상에 출력 
print(len(students)) #컨테이너 자료형 값의 갯수를 반환 ->길이 

#print(sum(students))  #모든 함수가 모든 자료형에 사용가능한것은 아니다.


#내장함수 sorted #컨테이너 자료형에만 적용됨
print(sorted(students)) # (기본)오름차순 정렬

#내림차순 정렬
print(sorted(students, reverse=True))

#익명함수 lanmbda
#사용자 정의함수 중, 이름을 붙일 필요가 없다고 판단해서 익명으로 냅둔함수, ->일회성으로 사용

a= (lambda x:-x) (-1)
print(a)

#흔한 사용 방식 
example= [(0,2),(2,3),(1,4),(0,-1),(100,-5)]

print(type(example)) #<class 'list'>
#print(type(example[0])) #

#정렬하려고 합니다!
example_a= sorted(example)
#정렬 -> 기준이 필요

# 2번째 값기준, 내림차순 정렬
example_b = sorted(example,key=lambda x:-x[1])

#example
#[(0,2),(2,3),(1,4),(0,-1),(100,-5)]

#첫번째 (0,2) -> -2(이걸 기준으로 삼겠다!)
#두번째 (2,3) -> -3
#세번째 (1,4) -> -4
#네번쨰 (0,-1) -> 1
#다섯번째 (100,-5) -> 5
# 람다함수를 거쳐서 나온 값을 기준으로 오름차분

print(example_b)
#[(1, 4), (2, 3), (0, 2), (0, -1), (100, -5)] 키라고 하는걸 이걸 걸쳐서 나오는걸 기준으로 오름차순으로 나온다는거구나! 

# 자료형마다 특징이 다 달라서!

# 리스트 메서드
# 순서0, 변경0, 중복0

numbers = [10,20,30,40,50]

#추가 -> 순서가 있게 추가(맨끝에)

numbers.append(60)
print(numbers)
# 나 자신을 바꿀 수가 있기 떄문에 (변경0)
# 새로 반환되는 리스트가 아닌 기존 numbers에 추가 
#->[10, 20, 30, 40, 50, 60]추가된걸 볼 수 있음

#삭제
#삭제: 위치(순서0)를 기준으로 삭제
numbers.pop(1)
print(numbers)
#[10, 30, 40, 50, 60] 이렇게 나옴 1번째 숫자 삭제됨

# 추가: 위치를 기준으로 추가 
numbers.insert(1,200)
print(numbers) #->[10, 200, 30, 40, 50, 60] 이렇게 첫번째에 추가됨

#추가여러개
numbers.extend([1,2,3,4])

#문자열
#순서0, 변경X, 중복0

word = 'helllllo'
print(word)

new_word=word.replace('l','x')
print(new_word)

#딕셔너리 
#순서X (키-값), 변경O, 중복X (키값의 중복 안됨)

students = {'kyle':10, 'jun':23, 'alex':30}
print(students['kyle'])

#값조회
print(students.get('ken')) #->None이라고 나옴 -> 조회하고자 하는 값이 없더라도 작동됨

students.update({'ken:40'})
print(students)

