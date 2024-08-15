a_list = []
b_list = [] 

for i in range(3):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

for i in range(3):
    if a_list.count(a_list[i]) == 1:
        a4 = a_list[i]
    if b_list.count(b_list[i]) == 1:
        b4 = b_list[i]
    

print(a4, b4)