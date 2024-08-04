t = int(input())
q = 25
d = 10
n = 5
p = 1

for i in range(t):
    c = int(input())
    print(c//q, c%q//d, c%q%d//n, c%q%d%n//p)
    