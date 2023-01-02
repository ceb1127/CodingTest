x, y, w, h = map(int, input().split())

# 길이 : w-x, h-y

print(min(x,y,w-x,h-y)) 

