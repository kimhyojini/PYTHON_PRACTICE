# [실습 1]
# 다음의 리스트에서 소숫점을 제외한 평균값을 구하시오. 
# ex) 3.1724일 경우 3을 출력
nums = [1, 7, 2, 3, 6, 1, 2, 5, 3, 4, 8, 7]

mean=sum(nums)/len(nums)
answer=int(mean)
print(answer)



mean=sum(nums)/len(nums)
answer=str(mean)   #원래는 4.083333이 나오는데, int를 (mean)앞에 넣으면 4로 딱 떨어짐 #문자열로 변경가능!! 
print(answer)
print(type(answer))
# print(answer) # 4

