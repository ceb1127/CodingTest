import sys
#sys.setrecursionlimit( 10** 6 )
input = sys.stdin.readline

N = int(input())
stairs = [0]*301 # 입력 받는 배열
dp = [0]*301 #값을 저장하는 배열

for i in range(1,N+1):
    stairs[i] = int(input())

def stair():
    # 계단이 1칸일 경우
    if N == 1:
        return stairs[1]
    
    # 계단이 2칸일 경우
    if N == 2:
        return stairs[1] + stairs[2]

    # 계단이 3칸일 경우
    if N == 3:
        return max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    # dp 배열 초기화
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    
    #점화식
    for i in range(4,N+1):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])


    return dp[N]

print(int(stair()))

     


    