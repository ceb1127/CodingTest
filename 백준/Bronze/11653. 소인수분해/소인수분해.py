N = int(input())

if N == 1 :
    print('')

for i in range(2,N+1) : #2부터 나누기
    if N % i == 0 : # 해당숫자로 나누어 떨어지면
        while N % i == 0 :
            print(i)
            N = N / i
        
        