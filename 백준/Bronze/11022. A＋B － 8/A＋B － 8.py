import sys

T = int(input())

for i in range(1,T+1) :
    A, B = map(int, sys.stdin.readline().split())
    C = A + B
    print("Case #{}: {} + {} = {}".format(i,A, B, C))