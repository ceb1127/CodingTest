# 1그룹 : 1/1
# 2그룹 : 1/2, 2/1 분자+1, 분모-1
# 3그룹 : 3/1, 2/2, 1/3 분자-1, 분모+1
# 1 2 3 4 5 6 7 

# num 5입력-> line 3 -> 2/2
# num 
  
num = int(input())
line = 1

while num > line:
    num -= line # 5 1 > 4 2 > 2 3
    line+=1

if line % 2 == 0:
    a = num
    b = line - num + 1
        
else :
    a = line - num + 1
    b = num
    
print(a,'/',b,sep='')
        