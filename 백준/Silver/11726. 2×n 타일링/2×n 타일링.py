import sys
input = sys.stdin.readline

n = int(input())
#square = [0]*(1000+1)
dp = [0]*(1000+1) 

dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n] % 10007)