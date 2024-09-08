import sys
input = sys.stdin.readline

def make_1(X): 
    cnt = [0]*(1000000+1) #최소 연산횟수 저장
    cnt[1] = 0
    #최소값 갱신
    #cnt[i-1] + 1
    #cnt[i/2] + 1
    #cnt[i/3] + 1

    for i in range(2, X+1):
        cnt[i] = cnt[i-1] + 1
        if i % 2 == 0 :
            cnt[i] = min(cnt[i], cnt[i//2] + 1)
        if i % 3 == 0 :
            cnt[i] = min(cnt[i], cnt[i//3] + 1)

    return cnt[X]

X = int(input())
print(make_1(X))




