# 2071. 평균값 구하기 D1
T = int(input())
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    avg = 0
    avg = round(sum(num)/len(num))
    print("#{} {}".format(test_case, avg))
