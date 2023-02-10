# 1) D를 모두 구해놓음
# 2) 입출력

import sys

MAX = 1000000 #최대값 설정
d = [1]*(MAX+1) #DP 1로 초기화
s = [0]*(MAX+1) #s : 값 누적 리스트

for i in range(2,MAX+1):
    j = 1
    while i*j <= MAX:
        # i의 배수에 값 추가 
        d[i*j] += i
        j += 1

for i in range(1,MAX+1):
    s[i] = s[i-1] + d[i] #누적 값 계산


t = int(input())
answer = []

for _ in range(t) :
    n = int(sys.stdin.readline())
    answer.append(s[n])
print('\n'.join(map(str,answer))+'\n')

# 시간 복잡도 O(nlogn)