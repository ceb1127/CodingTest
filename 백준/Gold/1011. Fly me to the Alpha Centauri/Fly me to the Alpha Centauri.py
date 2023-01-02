import math

T = int(input())

count = 0       #최소 작동 횟수
result = []

for _ in range(T) :
    x, y = map(int,input().split())
    distance = y - x        # 주어진 값들간의 거리

    num = math.floor(math.sqrt(distance)) # 주어진 값들 사이의 거리에 루트 씌움 (제곱근), math.floor : 내림 기능 3.xxxx를 3으로 정수처리
    num_jegob = num**2      # 정수를 제곱근으로 갖는 제곱 수 (ex. 9 : 9의 제곱근은 3)

    if distance == num_jegob :
        count = (num*2) -1

    elif num_jegob < distance <= num_jegob + num :
        count = (num*2)

    elif (num_jegob + num) < distance:
        count = (num*2) +1
    
    elif distance < 4 :
        count = distance
    result.append(count)

for x in result :
    print(x)