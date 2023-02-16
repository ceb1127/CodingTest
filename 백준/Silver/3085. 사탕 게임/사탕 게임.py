# 임의의 두칸을 변경했을 때 정답에 변화가 있는 것은 최대 3개의 행과 열임을 이용

def check(a, start_row, end_row, start_col, end_col) :
    n = len(a)
    answer = 1
    for i in range(start_row,end_row+1):
        cnt = 1
        for j in range(1,n) :
            if a[i][j] == a[i][j-1] :
                cnt += 1
            else :
                cnt = 1
            if answer < cnt :
                answer = cnt
    for i in range(start_col,end_col+1):
        cnt = 1
        for j in range(1,n) :
            if a[j][i] == a[j-1][i] :
                cnt += 1
            else :
                cnt = 1
            if answer < cnt :
                answer = cnt
    return answer


n = int(input())
a = [list(input()) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        if j+1 < n :
            a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
            temp = check(a, i, i, j, j+1 )
            if answer < temp:
                answer = temp
            a[i][j], a[i][j+1] = a[i][j+1],a[i][j]
        if i+1 < n:
            a[i][j], a[i+1][j] = a[i+1][j],a[i][j]
            temp = check(a, i, i+1, j, j)
            if answer < temp:
                answer = temp
            a[i][j], a[i+1][j] = a[i+1][j],a[i][j]
print(answer)

''' 
 1 ) 왜 시간초과 ? 
 # 시간복잡도 먼저 계산해보고 부르트포수(완전탐색)인거 확인 . 1억 = 1초
import sys
input = sys.stdin.readline
# 몇개 먹을 수 있는지 찾는 함수
def check(a) :
    n = len(a)
    answer = 1

    #한칸(i,j) 골라서 인접한 오른쪽, 아래 검사
    for i in range(n) : 
        #가로줄 순회
        cnt = 1 # 첨 시작
        for j in range(1,n):
            cnt = 1 
            for j in range(1,n) :
                if a[i][j] == a[i][j-1] : #이전과 같다면 +1
                    cnt += 1
                else :
                    cnt = 1   # 다르면 1
                # 현재 cnt가 더 크면 answer 갱신
                if answer < cnt :
                    answer = cnt

            #세로줄 순회
            cnt = 1
            for j in range(1,n):
                if a[j][i]== a[j-1][i] : 
                    cnt += 1
                else: 
                    cnt = 1
                if answer < cnt :
                    answer = cnt
    return answer

n = int(input())
a = [list(input()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
    # 행 : 오른쪽 교환 -> 계산 . 최대값이면 적용 -> 원래상태로 돌아가기 
        if j+1 < n :
            a[i][j],a[i][j+1] = a[i][j+1],a[i][j] #바꾸기 swap
            temp = check(a) #인접한 것을 바꿨을 때 가장 긴 연속 부분 찾아내는 함수 check
            if answer < temp:
                answer = temp
            a[i][j],a[i][j+1] = a[i][j+1],a[i][j] #원래대로
    # 열 : 아래 교환 -> 계산 . 최대값이면 계산 -> 원래상태로 돌아가기
        if i+1 < n :
            a[i][j],a[i+1][j] = a[i+1][j],a[i][j]
            temp = check(a)
            if answer < temp:
                answer = temp
            a[i][j],a[i+1][j] = a[i+1][j],a[i][j]
print(answer)


'''


 