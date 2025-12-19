name = "kimhyojin"
age = 29
is_male = False

print(type(name))

# 사용자 입력

# 내장함수 input을 통해 사용자에게 입력받습니다.
name = input ('이름을 입력해주세요 : ')
print(name)

age = input('나이를 입력해 주세요 : ')
print(age)

# 내장함수 input을 통해 입력받은 자료형은 항상 str
print(type(age))


print("===== 출력 =====")
# 터미널 상에서 보여주기 위함입니다.
# print 내장함수를 사용합니다.
word1 = 'hello'
word2 = 'python'

print(word1, word2)
# 콤마(,)를 기준으로 여러 변수 출력 가능
# 공백(default가 공백)을 기준으로 연결되어 한줄 출력
print(word1, word2)