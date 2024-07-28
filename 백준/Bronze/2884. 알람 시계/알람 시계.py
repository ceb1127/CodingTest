h, m = map(int,input().split())

if m >= 45 : 
    print(h, m-45)
else : 
    m += 15
    if h != 0 :
        h -= 1
    else:
        h = 23
    print(h, m)
  