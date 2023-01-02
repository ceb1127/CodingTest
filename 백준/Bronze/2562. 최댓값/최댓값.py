list_a = []

for i in range(9) :
    list_a.append(int(input()))

print(max(list_a))
print(list_a.index(max(list_a))+1)
