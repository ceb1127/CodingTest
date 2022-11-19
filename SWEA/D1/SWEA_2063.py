# 2063. 중간값 찾기 D1
T = int(input())
for test_case in range(1, T + 1):
    N = list(map(int, input().split()))
    N.sort()
    index = (T-1)//2
    mean_n = N[index]
    print("{}".format(mean_n))