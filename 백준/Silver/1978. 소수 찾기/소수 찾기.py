def prime(x) :
    if x < 2 :
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


n = int(input())
a = list(map(int, input().split()))
answer = 0

for x in  a:
    if prime(x):
        answer += 1
print(answer)

