n = int(input())
num = list(map(int, input().split()))
cnt = 0

for su in num :
    if su == 1 :
       continue
    for i in range(2, su):
      if su % i == 0:
         break
    else : 
        cnt+=1

print(cnt)

