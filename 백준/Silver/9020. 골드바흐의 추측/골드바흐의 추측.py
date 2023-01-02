prime_list = [False, False] + [True]*10000 #인덱스 0, 1에 false값 넣어주고 나머지가 True인 길이 10002인 배열 선언


for i in range(2,100+1) : #입력값이 10000이기때문에 절반인 101만큼 
    if prime_list[i] == True :
        for j in range(i + i, 10001, i) :
            prime_list[j] = False

T = int(input())

for _ in range(T) :
    N = int(input()) # 8
    num = N // 2 # N을 2로 나눈 나머지 . #0

    for j in range(num, 1, -1) :
        if prime_list[N - j] and prime_list[j] :
            print(j, N - j)
            break