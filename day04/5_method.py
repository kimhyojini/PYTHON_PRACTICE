#메서드
# 특정 자료형에 딸려 있는 함수 


#리스트 

numbers = [10,20,30,40,50]

# 추가 
# append 메서드를 통해 가장 마지막 위치에 새로운 원소 딱 하나만 추가 

# 삭제 : pop
# 위치를 기준으로 삭제 
deleted_value = numbers.pop(1)

# 삭제: remove 메서드 
# 값을 기준으로 삭제
numbers.remove(10000)
print(numbers) 

# 값 세기 
numbers.extend([10,10,20,40])
print(numbers)
cnt=numbers.count(10) # 리스트 자체를 바꾸지 않습니다.
print(cnt)

# 정렬 ->list는 바꿀 수 있음 sort() 메서드 
# sorted 내장함수와의 차이점
# 내장함수 sorted() : 전달받은 컨테이너를 정렬하여, "새로운 리스트"를 반환
# 메서드 sort() : 기존의 리스트 자체를 변경 -> 정렬한다.
numbers.sort(key=lambda x:-x) 

numbers.sort(key=lambda x:x%3, -x) #두가지 기준으로 정렬 
print(numbers) 

