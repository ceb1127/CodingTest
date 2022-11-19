# 2068. 최대수 구하기 D1
T = int(input())
for test_case in range(1, T + 1):
    su = list(map(int, input().split()))
    max_num = 0
    for i in range(len(su)) :
        max_num = max(su)
    print("#{} {}".format(test_case, max_num))