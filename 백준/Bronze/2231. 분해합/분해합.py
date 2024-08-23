N = int(input())

for i in range(N+1):
    degit_sum = i + sum(map(int, str(i)))
    if degit_sum == N :
        print(i)
        break
    elif i == N :
        print(0)