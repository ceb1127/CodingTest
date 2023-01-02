import math #pi 함수를 사용하기 위해 math모듈을 불러들였다.

r = int(input())
print(f'{r*r*math.pi:.6f}') # 원의 넓이
print(f'{2*r*r:.6f}') # 택시 기하학 원의 넓이 = 마름모 넓이