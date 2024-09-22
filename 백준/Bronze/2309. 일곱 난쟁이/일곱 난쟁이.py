import sys
input = sys.stdin.readline

lst = [int(input()) for _ in range(9)]

def solve(): 
    N = 9
    num = sum(lst) - 100
    for i in range(0, N-1):
        for j in range(i+1, N):
             if lst[i] + lst[j] == num :
                 return lst[i], lst[j]

n, m = solve()
for i in sorted(lst):
    if i != n and i != m :
        print(i)

