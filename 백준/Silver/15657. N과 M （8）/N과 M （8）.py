# 중복가능, 비내림차순
import sys

n, m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
c = [False]*(n+1)
a = [0]*m

def go(index,start,n,m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    
    for i in range(start,n):
        c[i] = True
        a[index] = num[i]
        go(index+1,i,n,m)
        c[i] = False

go(0,0,n,m)