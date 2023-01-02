num = int(input())
score = list(map(int,input().split()))
M = max(score)

for i in range(num) :
    score[i] = score[i]/M*100
    avg = sum(score)/num

print(avg)