level = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
score = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]

total_score = 0
result = 0

for i in range(20):
    sub, sco, gra = input().split()
    if gra != 'P' :
        total_score += float(sco)
        result += float(sco)*score[level.index(gra)]

print('%.6f' %(result/total_score))