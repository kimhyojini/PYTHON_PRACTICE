# [실습 7]
# 다음과 같은 api 데이터가 있을 때, 모든 유저들의 이름을 모아보시오.
users = {
    'total_user': 3,
    'information': [
        {'name': 'alex', 'age': 3, 'license': True},
        {'name': 'june', 'age': 7, 'license': False},
        {'name': 'peter', 'age': 4, 'license': False}
    ]
}
names=[]
for user in users['information']:
    names.append(user['name'])
print(names)



names = []
# 로직 작성
#내가쓴것
# users.add('names')
print(names)  # ['alex', 'june', 'peter']

#실제답변
for user in users['information']:
    names.append(user['name'])
    
print(names)


# scores = [10,20,30,40,50,60,700,90, 80, 70]

# #()과[]의 차이점 확인
# print(scores[-2])
# scores[3]=400
# print(scores)

# #[]더 깊게 이해하기 
# user = {'name': 'alex', 'age': 20}
# user = 
# print(user['name'])  # alex
# print(user['age'])   # 20
