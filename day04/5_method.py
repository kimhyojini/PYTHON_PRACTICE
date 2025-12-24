#메서드
# 특정 자료형에 딸려 있는 함수 


#리스트 

numbers = [10,20,30,40,50]

# 추가 
# append 메서드를 통해 가장 마지막 위치에 새로운 원소 딱 하나만 추가 

# 삭제 : pop
# 위치를 기준으로 삭제 
deleted_value = numbers.pop()

# 삭제: remove 메서드 
# 값을 기준으로 삭제
numbers.remove(10000)
print(numbers) 