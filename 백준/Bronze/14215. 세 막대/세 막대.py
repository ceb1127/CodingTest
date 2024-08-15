num_list = list(map(int,input().split()))
num_list.sort()
a, b, c = num_list

if a + b <= c:
    c = a + b -1 

print(a+b+c)
