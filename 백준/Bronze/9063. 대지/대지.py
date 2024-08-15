n = int(input())
a_list = []
b_list = []

for i in range(n):
    a, b = map(int,input().split())
    a_list.append(a)
    b_list.append(b)


print( (max(a_list)-min(a_list)) *  (max(b_list)-min(b_list))  )
        
    
        
    