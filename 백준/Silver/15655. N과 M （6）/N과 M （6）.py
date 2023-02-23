n, m = map(int,input().split())
num = list(map(int, input().split()))
num.sort()
c = [False]*(n+1)
a = [0]*m

def go(index, start, n, m):
    if index == m:
        print(' '.join(map(str,a)))
        return
    
    for i in range(start, n):
        if c[i] :
            continue
        c[i] = True
        a[index] = num[i]
        go(index+1,i+1, n,m)
        c[i] = False
     

go(0,0,n,m)