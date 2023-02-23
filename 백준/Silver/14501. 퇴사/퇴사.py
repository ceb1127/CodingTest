# 날짜, 수입 중요 -> 함수 매개변수
# sum : day-1일까지의 수익
# 1 ~ N일 == 0 ~ n-1일
n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)
for i in range(1,n+1):
    t[i],p[i] = map(int,input().split())
ans = 0

def go(day, sum):
    global ans
    if day == n+1 : # 정답을 찾은 경우 : day == n+1
        ans = max(ans, sum)
        return
    
    if day > n+1 : # 불가능 한 경우 : day > n+1(퇴사일)
        return

    # 상담 x : 날짜 +1, 수익 
    go(day+1,sum)
    # 상담 o : 날짜 +t[day]만큼, sum+p[day]
    go(day+t[day], sum+p[day])


go(1,0)
print(ans)

 
