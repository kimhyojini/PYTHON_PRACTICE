# 떡잎마을 반장선거
# 후보가 없는 반장선거 
# 표가 발생하면, 자동 입후보 되는 구조

votes = ['짱구','짱구','수지','짱구','훈이','맹구',
        '수지','수지','수지','짱구','유리','철수']

count = {}
result = {}

for name in votes :
    if name not in count:
        count[name] = 1
    else:
        count[name] += 1
print(count) 

for vote in votes:
    if vote not in result: #입후보 안된 경우에만, 입후보 하면서 1표 집계
        result[vote] = 1 
    else:
        result[vote] += 1

print(result)

#최다 특표 인원 찾기(동점없을때)
max_counts = 0
max_name = ""

for k,v in result.items():
    if v > max_counts:
        max_counts = v
        manx_name = k
        
print(f'반장은 {max_counts}득표한 {max_name}가 되었습니다.')
winner = max(count, key=count.get)

print('반장', winner)
        

# 누가 반장이 될까요?

