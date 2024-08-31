n_list = [] 

for i in range(5) :
    n_list.append(int(input()))

n_list.sort()

print(int(sum(n_list)/len(n_list)))
print(n_list[2])
