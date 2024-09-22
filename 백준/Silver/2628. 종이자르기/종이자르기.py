import sys
input = sys.stdin.readline

#[1] 가능한 가로, 세로 자르는 위치를 저장 후 정렬
C,R = map(int,input().split())
c_lst = [0,C]
r_lst = [0,R]

N = int(input())
for _ in range(N):
    t, n = map(int,input().split())
    if t == 0:
        r_lst.append(n)
    else:
        c_lst.append(n)

c_lst.sort()
r_lst.sort()

#[2] 가장 긴 길이 찾기
c_mx = 0
for i in range(1,len(c_lst)):
    c_mx = max(c_mx, c_lst[i]-c_lst[i-1])

r_mx = 0
for i in range(1,len(r_lst)):
    r_mx = max(r_mx, r_lst[i]-r_lst[i-1])

print(c_mx*r_mx)
    