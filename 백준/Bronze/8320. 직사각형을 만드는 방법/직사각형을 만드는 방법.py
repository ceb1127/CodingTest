import sys
input = sys.stdin.readline

N = int(input())

# [2] 규칙성 : 몫 연산을 통해서 처리
ans = N
for i in range(2,N):
    n = N//i - (i-1)
    if n<1:
        break
    ans+=n
print(ans)

# [1]가로 세로 다 탐색
# ans = 0
# for i in range(1,N+1):
#    for j in range(i,N+1):
#        if i*j <= N :
#            ans += 1
#print(ans)
            