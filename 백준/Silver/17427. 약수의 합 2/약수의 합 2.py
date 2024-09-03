# g(2) = f(1) + f(2)  #i의 약수의 합 + 2의 약수의 합
N = int(input())
total = 0

for i in range(1,N+1):
     total += (( N // i )*i) 
print(total)

#f(1) + f(2) + f(3) ... 