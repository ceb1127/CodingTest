# 에라토스테네스의 체 이용
MAX = 1000000
check = [0]*(MAX+1)
check[0] = check[1] = True #지워짐

for i in range(2,MAX+1) :
    if not check[i] : # 지워지지않음
        j = i + i
        while j <= MAX :
            check[j] = True #지움 
            j += i

m, n = map(int, input().split())
for i in range(m,n+1):
    if check[i] == False :
        print(i)