# 1부터 n까지 자연수 중에서 중복 없이 M개를 고른 수열
# 오름차순 -> start 넣어서 그것보다 큰 수로
n, m = map(int, input().split())
c = [False]*(n+1)
a = [0]*m

def go(index, start, n, m):
    if index == m :
        print(' '.join(map(str,a)))
        return

    for i in range(start, n+1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1,i+1, n, m) #다음 수는 a[index]인 i보다 더 큰수에서 시작
        c[i] = False
    

go(0, 1, n, m)

