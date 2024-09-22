import sys
input = sys.stdin.readline

N = int(input())

# [1]가로 세로 다 탐색
ans = 0
for i in range(1,N+1):
    for j in range(i,N+1):
        if i*j <= N :
            ans += 1

print(ans)
            