N = int(input())
score = list(map(int,input().split()))
result = []

for i in range(N):
    max_score = max(score)
    result.append(score[i]/max_score*100)
    
print(sum(result)/len(result))