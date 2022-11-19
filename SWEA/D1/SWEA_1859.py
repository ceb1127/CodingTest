#1859. 백만장자 프로젝트 D2
T = int(input())
for test_case in range(1, T + 1):
    day = int(input())
    price = list(map(int, input().split()))
    sum = 0
    max_price = 0
    for i in range(day-1, -1 ,-1) :
        if price[i] > max_price :
            max_price = price[i]
        else :
            sum += max_price - price[i]
    print("#{} {}".format(str(test_case), sum))

