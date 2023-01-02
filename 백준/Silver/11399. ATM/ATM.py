from itertools import accumulate

su = int(input())
time = list(map(int,input().split()))

time.sort() #오름차순 정렬 
# print(time) # [1,2,3,3,4]

result = list(accumulate(time)) # accumulate :  누적 합 구하기

print(sum(result))
