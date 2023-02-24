# 백트래킹

# index번째 수를 결정하면, 0~index번째 수는 변하지 않는다.
# 따라서 모든 sign[k][index] (0<=k<index)를 go(index)에서 검사할 수 있다.

# 부호와 합이 일치하는지 확인하는 함수
def check(index): #index번째 수를 결정
    s = 0
    for i in range(index,-1,-1):
        s += ans[i]
        if sign[i][index] == 0:
            if s != 0:
                return False
        elif sign[i][index] < 0:
            if s >= 0:
                return False
        elif sign[i][index] > 0:
            if s <= 0:
                return False
    return True

# 실행 함수
def go(index):
    if index == n:
        return True
    if sign[index][index] == 0:
        ans[index] = 0
        return check(index) and go(index+1)

    for i in range(1, 11):
        ans[index] = i * sign[index][index]
        if check(index) and go(index+1):
            return True
    return False

n = int(input())
s = input()
sign = [[0]*n for _ in range(n)]
ans = [0]*n
cnt = 0
for i in range(n):
    for j in range(i,n):
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1

go(0)
print(' '.join(map(str,ans)))
'''
# 브루트포스 -> 시간 초과 21^10

# 부호와 합이 일치하는지 확인하는 함수
def ok():
    for i in range(n) :
        s = 0
        for j in range(i,n) :
            s += ans[j]   
            if sign[i][j] == 0:   #sign[i][j] = 출력될 정수 s[i]의 부호  
                if s != 0 :
                    return False
            elif sign[i][j] > 0 :
                if s <= 0 :
                    return False
            elif sign[i][j] < 0 :
                if s >= 0 :
                    return False
    return True
        
# 실행 함수
def go(index):
    if index == n:
        return ok()
    for i in range(-10, 11):
        ans[index] = i
        if go(index+1):
            return True
    return False

n = int(input())
s = input()
sign = [[0]*n for _ in range(n)]
ans = [0]*n
cnt = 0
for i in range(n) :
    for j in range(i,n) :
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1

go(0)
print(' '.join(map(str,ans)))
'''