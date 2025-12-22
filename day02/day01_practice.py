# 커피 구매와 거스름돈 계산 프로그램

money = int(input('현재 잔액을 입력해 주세요')) # 현재 보유 금액

# 코드 입력

price = 2000

# 몫을 나타내는 연산자 : //
count = money // price #커피구매
# 나머지를 나타내는 연산자 : %
change = money % price #거스름돈



print(count)
print(change)


