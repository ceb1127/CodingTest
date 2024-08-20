N, M = map(int,input().split())
card = sorted(list(map(int,input().split())))
sum_card = []

for i in range(len(card)):
    for j in range(i+1,len(card)):
        for k in range(j+1,len(card)):
            sum_card.append(card[i]+card[j]+card[k])

if M in sum_card :
    print(M)
else:
    sum_card.append(M)
    sum_card.sort()
    x_inx = sum_card.index(M)
    print(sum_card[x_inx-1])







