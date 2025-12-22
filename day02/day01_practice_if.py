# 커피 구매와 거스름돈 계산 프로그램

# money = int(input('현재 잔액을 입력해 주세요')) # 현재 보유 금액

# 코드 입력

# price = 2000

# 몫을 나타내는 연산자 : //
# count = money // price #커피구매
# 나머지를 나타내는 연산자 : %
# change = money % price #거스름돈



# print(count)
# print(change)

# 2.버스 요금 계산
    #나이(age)와 결제 수단(card_type: "일반" 또는 "정기권")을 입력받아 버스요금을 출력하세요.
    #정기권이면 무조건 0원
    #정기권이 아니면 기존 나이 규칙 적용
    #7세 미만 또는 65세 이상: "무료"
    #7세 이상 19세 이하: "청소년 요금"
    #20세 이상 64세 이하: "성인 요금"

## 2. 버스 요금 계산

age = int(input('나이를 입력해 주세요.'))
card_type = input('결제 수단을 입력해 주세요 :')

if card_type == '정기권':
    print('0원')
elif age < 7 or age >= 65 :
    print('무료')
elif age <=19 :
    print('청소년 요금')
else : 
    print('성인 요금')