M = int(input())
N = int(input())

sosu_list = []

def prime(num) : # 소수 함수
    if num == 1: 
        return 0 #소수가 아닐 경우 리턴 0
    elif num == 2:
        return num #소수일 경우 리턴 숫자
    for i in range(2,num) :
        if num % i == 0 :
            return 0
    return num

for i in range(M,N+1) :
    if prime(i)>0 : # 리스트에서 0보다 큰 값 즉 소수 출력
        sosu_list.append(prime(i)) #0이 아닌 소수 리스트에 추가
    
if len(sosu_list)>0: 
    # print(sosu_list) # 소수 모두 출력 
    print(sum(sosu_list)) # 소수 리스트 값 출력
    print(min(sosu_list)) # 소수 리스트 중 가장 작은 소수 출력
else:
    print(-1)    


