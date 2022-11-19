#2072 홀수만 더하기 D1
T = int(input())
for test_case in range(1, T + 1):
    su = list(map(int, input().split()))
    sum = 0
    for i in range(len(su)) :
        if su[i] % 2 == 1 :
            sum += su[i]
    print("#"+str(test_case)+" "+str(sum))