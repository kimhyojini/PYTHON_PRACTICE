# 조건문

print(2 < 5)
if 2 != 5: # if True 혹은 False로 해석될 수 있는 조건이 와야 함   
        print('조건이 참입니다.')
        print('같은 들여쓰기 수준이라면')
        print('동일한 코드블럭입니다.')
        
print('여기는? 조건문과 상관없이 무조건 나옴, 위에가 거짓일지라도')

# 2) 비교연산 + 산술연산 조합
number = 6
if number % 2 == 1:
    print(f'{number}는 홀수입니다.')