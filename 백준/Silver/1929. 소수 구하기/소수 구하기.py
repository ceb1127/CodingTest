M, N = map(int, input().split())

def prime(num) :
    if num == 1:
        return False
    else : 
        for i in range(2, int(num**0.5)+1): #제곱근까지 검사하여 소수인지 아닌지 판별
            if num % i == 0 :
                return False
        return True

for i in range(M,N+1) : 
    if prime(i) :
        print(i)