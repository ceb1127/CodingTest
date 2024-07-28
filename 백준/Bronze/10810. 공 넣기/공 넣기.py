N, M = map(int,input().split())
a_list = [0]*N

for i in range(M):
    a, b, c = map(int,input().split())
    for j in range(a, b+1):
        a_list[j-1] = c
    
for i in range(len(a_list)):
    print(a_list[i], end=" ")
    

