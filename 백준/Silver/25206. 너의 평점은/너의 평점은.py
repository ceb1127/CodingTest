grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 
         'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

total_score = 0
result = 0

for i in range(20):
    sub, sco, gra = input().split()
    if gra != 'P' :
        total_score += float(sco)
        result += float(sco)*grade[gra]

print('%.6f' %(result/total_score))