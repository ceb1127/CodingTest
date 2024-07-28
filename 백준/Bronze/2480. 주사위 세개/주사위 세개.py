a, b, c = map(int,input().split())
su = int()

if a == b == c :
    print(10000+1000*a)
elif a == b or a == c or b == c :
    if a == b or a == c:
        print(1000+100*a)
    elif b == c:
        print(1000+100*b)
else :
  if a > b and a > c: 
    print(a*100)
  elif b > a and b > c:
    print(b*100)
  elif c > a and c > b:
    print(c*100)