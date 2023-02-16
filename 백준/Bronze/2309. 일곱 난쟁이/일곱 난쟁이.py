import sys
# 합 100 넘는 2명 빼기
height = [ int(input()) for i in range(9) ]
height.sort()
total = sum(height)
for i in range(0,len(height)) :
    for j in range(i+1,len(height)):
        if total - height[i] - height[j] == 100 : #아홉난쟁이 합- 가짜난쟁이 합 = 100
            for k in range(len(height)) : 
                if i == k or j == k: 
                    continue #가짜 난쟁이들 제외
                print(height[k])
            sys.exit(0)
