table = [list(map(int, input().split())) for _ in range(9) ]

max_value = 0
max_row = 0 
max_col = 0

for row in range(9):
    for col in range(9):
        if max_value <= table[row][col]:
            max_row = row+1
            max_col = col+ 1
            max_value = table[row][col]
            
print(max_value)
print(max_row, max_col)
            