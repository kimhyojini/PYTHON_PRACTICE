#문자열
    #순서:o
    #변경:x
    #중복:o
word = 'merry christmas!!!!!'
print(word)

print(len(word)) #20개짜리 각각의 모음집


#문자열 분할: split
#특정한 구분자를 기준으로 문자열을 나눠서, 리스트를 반환
# word_list = word.split(' ') #자기자신을 바꾸지 않고, 리스트를 반환 
# print(word_list) 

# #언제사용?
# students = input('학생의 이름 명단을 입력해 주세요.')

# student_list = students.split(',')
# print(type(students))
# print(student_list)

# 문자열 합치기: join()
string_list = ['merry','christmas','!!','happy','holiday','!!']
print(len(string_list))
string_join =''.join(string_list)
print(string_join)