# n과 m + 추가 조건

# 최소 한개의 모음과 최소 두개의 자음 함수
def check(password) : 
    ja = 0
    mo = 0
    for x in password:
        if x in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja >=2 and mo >=1

# 암호 만들기 함수 
def go(n, alpha, password, i) : 
    '''
    n : 만들어야 하는 암호 길이
    alpha : 사용할 수 있는 알파벳
    password : 현재까지 만든 암호
    i : 사용할지 말지 결정해야하는 알파벳의 인덱스
    '''
    if len(password) == n : # 정답을 찾은 경우
        if check(password) :
            print(password)
        return
    
    if i >= len(alpha): # 불가능한 경우 : 더이상 선택할 수 있는 알파벳이 없으면 재귀함수 호출 불가
        return
    
    go(n, alpha, password+alpha[i], i+1) # i번째를 사용하는 경우 호출
    go(n, alpha, password, i+1) #i번째 사용하지 않는 경우 호출


L, C = map(int,input().split())
a = input().split()
a.sort()
go(L,a,"",0)