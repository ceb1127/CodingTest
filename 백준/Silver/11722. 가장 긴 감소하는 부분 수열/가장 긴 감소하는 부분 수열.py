import sys
input = sys.stdin.readline

N = int(input())
n_list = list(map(int,input().split()))
dp = [1]*(N+1)#감소하는 수열 길이 저장

for i in range(N) :
   for j in range(i):
        if n_list[j] > n_list[i] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))