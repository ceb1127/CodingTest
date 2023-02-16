import sys

#에라토스테네스 체 이용해서 소수 미리 계산 : 에라토스테네스의 체 처럼 연산이 많은 경우 pypy3
MAX = 1000000
check = [0]*(MAX+1)
check[0] = check[1] = True

# prime에 소수를 추가, 배수를 모두 제거
prime = []
for i in range(2, MAX+1) :
    if not check[i] :
        prime.append(i)
        j = i + i 
        while j <= MAX :
            check[j] = True
            j += i
prime = prime[1:]

# 골드바흐의 추측, p가 작은 수부터 큰 수로 돌기때문에 n-p를 구함 : A+B = N
while True:
    n = int(sys.stdin.readline())
    if n == 0 :
        break
    for p in prime:
        if check[n-p] == False:
            print("{0} = {1} + {2}".format(n,p,n-p))
            break