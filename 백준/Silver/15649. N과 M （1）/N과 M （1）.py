# 1부터 n까지 중복없이 m개
n, m = map(int, input().split())
c = [False]*(n+1) # i를 사용했으면 true
a = [0]*m # 수열 저장 

def go(index, n, m ):
    if index == m :
        print(' '.join(map(str,a))) #sys.stdout.write(' '.join(map(str,a))+'\n')
        return 
    for i in range(1, n+1) :
        if c[i] :
            continue #c[i]가 true라면 건너뜀. 사용했다는 의미
        # 건너뛰지 않았다면 수 i 사용
        c[i] = True
        a[index] = i

        go(index+1, n, m) #재귀함수 방식 : index+1해서 다음함수 호출 
        c[i] = False 

go(0,n,m)