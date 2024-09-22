import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
alst = [ n for n in range(1,N+1)]

for i in range(0,N):
    n,t = lst[i],alst[i]

    for j in range(i,i-n,-1):
        alst[j] = alst[j-1]
    alst[i-n] = t

print(*alst)