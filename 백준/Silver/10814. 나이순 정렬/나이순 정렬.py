n = int(input())
p_list = []


for i in range(n):
    a,b = map(str,input().split())
    p_list.append((int(a),b))

s_list = sorted(p_list,key = lambda x : x[0])
for i in s_list :
    print(*i)