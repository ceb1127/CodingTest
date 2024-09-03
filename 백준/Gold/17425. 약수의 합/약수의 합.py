import sys
input = sys.stdin.readline

T = int(input().strip())

MAX = 1000000 #최대값 설정

dp = [0]*(MAX+1) #dp 초기화 
sum_dp = [0]*(MAX+1) #값 누적 리스트 

# 약수의 합 계산
for i in range(1, MAX+1): # 1 2 3 4 5 
    for j in range(i,MAX+1,i): # 1 1 1 1 1 2 2 3 4 5 
        dp[j] += i

#print(dp)
# 1부터 i까지 약수의 합의 총합 계산
for i in range(1,MAX+1):
    sum_dp[i] = sum_dp[i-1]+dp[i]

for _ in range(T):
    n = int(input().strip())
    print(sum_dp[n])