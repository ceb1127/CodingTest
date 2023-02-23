# 중복 선택 가능
N, M = map(int,input().split())
c = [False]*(N+1)
a = [0]*M

def go( index, N, M ):
    if index == M :
        print(' '.join(map(str,a)))
        return
    
    for i in range(1,N+1):
        c[i] = True
        a[index] = i
        go(index+1, N, M)
        c[i] = False

go(0,N,M)