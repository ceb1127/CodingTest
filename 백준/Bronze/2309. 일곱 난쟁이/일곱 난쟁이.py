import sys
input = sys.stdin.readline
nan = []

for _ in range(9):
    nan.append(int(input().strip()))

from itertools import combinations
nan_final = list(combinations(nan,7))

for i in nan_final:
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
