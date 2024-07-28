a_list = []

for i in range(9):
    a_list.append(int(input()))
    

print(max(a_list))
print(a_list.index(max(a_list))+1)