n = int(input())
n_list = []
for _ in range(n):
    a, b = map(int,input().split())
    n_list.append((a,b))

s_list = sorted(n_list)
for i in s_list:
    print(*i)
    