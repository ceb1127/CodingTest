A = int(input())
B = int(input())
C = int(input())

result_list = list(str(A * B * C))

for i in range(10) : 
        print(result_list.count(str(i)))


