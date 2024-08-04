n, m = map(int, input().split())

A, B = [],[]

for i in range(n):
    a = list(map(int, input().split()))
    A.append(a)
             
for j in range(n):
    b = list(map(int, input().split()))
    B.append(b)
             
             
             
for row in range(n):
    for col in range(m):
       print(A[row][col] + B[row][col], end=" ")
    print()