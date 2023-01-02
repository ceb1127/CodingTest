n = int(input()) #테스트 케이스 입력

sosu = list(map(int,input().split()))

def prime(num) : #소수 함수 생성
    if num == 1:
        return False # 1은 소수가 아님 
    elif num == 2:
        return True # 2는 소수
    for i in range(2,num) : 
        if num % i == 0 : #2부터 num까지 숫자로 나누어 떨어지는 수는 소수가 아님
            return False
    return True
count = 0

for i in sosu :
    if prime(i) : #프라임 함수에 입력받은 값을 넣었을 때
        count += 1  #true 값이라면 count 증가
print(count)
