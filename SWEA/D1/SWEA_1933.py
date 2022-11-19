# 1933. 간단한 약수 D1
N = int(input())
for i in range(1,N+1):
    if N%i == 0 :
        print(i,end=" ")