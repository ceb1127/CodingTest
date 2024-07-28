numlist = []

for i in range(10):
    a = int(input())
    numlist.append(a%42)

print(len(set(numlist)))