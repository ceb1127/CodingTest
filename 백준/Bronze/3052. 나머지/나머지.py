result = []
count = {}

for i in range(10) :
    num = int(input())
    result.append(num % 42)
    
for i in result :
    try : count[i] += 1 #리스트에 이미 존재하는 값이면 +1
    except : count[i] = 1 #리스트에 없으면 1 출력 


print(len(count)) # 서로 다른 수 출력 