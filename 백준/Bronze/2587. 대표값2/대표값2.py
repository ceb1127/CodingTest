n_list = [] 
sum_num = 0

for i in range(5) :
    n = int(input())
    n_list.append(n)

n_list.sort()

for i in n_list:
    sum_num +=i

print(int(sum_num/len(n_list)))
print(n_list[2])
